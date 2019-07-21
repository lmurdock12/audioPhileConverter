from __future__ import print_function
from typing import List
import json
import logging
import sys
import requests
import time
import os
import re
import swagger_client as cris_client
from azure.storage.blob import BlockBlobService, PublicAccess


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format="%(message)s")

SUBSCRIPTION_KEYS = ["4f9c42b6bd3c45c3bf18fe22069e20d7","f4c27483b38c4c3eaac8d3c39618f08f","d928e4397dd24cddb7dad6a72f4f27d9","809ae668bd8e4350aa5c5db492222459","203ce901802a4819b2f3bf47859e7f75","86c80269a0d74ffeb69bd71bd3da9a84","f692dbd72b074e3ea2266012890ba4f5","9b3acd74a7e64b3ca151e64ca7748636","ce7a6e9ae0c544a286ed3c7d8e353532","e966fd341e4e4483984456a3b00dd846","e7112e69039e4953a6e59b4f056a79c9","8e46859b98454d71a027b49bbdd3f542","c544229e167841b0a52272905a8d0d79",]

HOST_NAME = "southcentralus.cris.ai"
PORT = 443

NAME = "Simple transcription"
DESCRIPTION = "Simple transcription description"

AUDIO_CONTAINER = "audio"
TRANSCRIPT_CONTAINER = "transcript"
ANALYSIS_CONTAINER = "analysis-json"

LOCALE = "en-US"
# RECORDINGS_BLOB_URI = "https://audiophilesdata.blob.core.windows.net/audio/Innovation01-30sec.mp3?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2019-06-16T00:16:17Z&st=2019-06-13T16:16:17Z&spr=https&sig=kVwhytCWgv7ER3b%2FiOTUvb7Mu9mHbNeHOQ2H9LODslc%3D"
RECORDINGS_BLOB_URI = "https://audiophilesdata.blob.core.windows.net/audio/{}?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2019-06-16T00:16:17Z&st=2019-06-13T16:16:17Z&spr=https&sig=kVwhytCWgv7ER3b%2FiOTUvb7Mu9mHbNeHOQ2H9LODslc%3D"

# Set subscription information when doing transcription with custom models
ADAPTED_ACOUSTIC_ID = None  # guid of a custom acoustic model
ADAPTED_LANGUAGE_ID = None  # guid of a custom language model

isTranscribing = False

def getOffset(elem):
    return elem["Offset"]

def getTranscript(data):
    transcript = ""
    for num in data['AudioFileResults']:
        for segment in sorted(num['SegmentResults'], key = lambda i: i['Offset']):
            for nBest in segment['NBest']:
                transcript += nBest['Display']
    return transcript

def diff(first, second):
    second = set(second)
    return [item for item in first if item not in second]

def transcribe(fileName):
    SUB_KEY_INDEX = 0
    logging.info("Starting transcription client...")
    isTranscribing = True

    # get blob service
    block_blob_service = BlockBlobService(account_name='audiophilesdata', account_key='HNRhdcv4TVEp8mcgDc0B7GfbzS3RnCEuBgGr71auzhZkd7mkHu6aBpHU1TBoZb3YTnM0SDEsiEP6jO4i8Q0D5g==')

    # configure API key authorization: subscription_key
    configuration = cris_client.Configuration()
    configuration.api_key['Ocp-Apim-Subscription-Key'] = SUBSCRIPTION_KEYS[SUB_KEY_INDEX]

    # create the client object and authenticate
    client = cris_client.ApiClient(configuration)

    # create an instance of the transcription api class
    transcription_api = cris_client.CustomSpeechTranscriptionsApi(api_client=client)

    # get all transcriptions for the subscription
    transcriptions: List[cris_client.Transcription] = transcription_api.get_transcriptions()

    logging.info("Deleting all existing completed transcriptions.")
    # delete all pre-existing completed transcriptions
    # if transcriptions are still running or not started, they will not be deleted
    for transcription in transcriptions:
        try:
            transcription_api.delete_transcription(transcription.id)
        except:
            print("There was an error deleting the id. But keep chugging.")
        

    logging.info("Creating transcriptions.")

    # Use base models for transcription. Comment this block if you are using a custom model.
    transcription_definition = cris_client.TranscriptionDefinition(
        name=NAME, description=DESCRIPTION, locale=LOCALE, recordings_url=RECORDINGS_BLOB_URI.format(fileName), properties={'AddWordLevelTimestamps':'True',"AddSentiment":"True"}
    )

    # Uncomment this block to use custom models for transcription.
    # Model information (ADAPTED_ACOUSTIC_ID and ADAPTED_LANGUAGE_ID) must be set above.
    # if ADAPTED_ACOUSTIC_ID is None or ADAPTED_LANGUAGE_ID is None:
    #     logging.info("Custom model ids must be set to when using custom models")
    # transcription_definition = cris_client.TranscriptionDefinition(
    #     name=NAME, description=DESCRIPTION, locale=LOCALE, recordings_url=RECORDINGS_BLOB_URI,
    #     models=[cris_client.ModelIdentity(ADAPTED_ACOUSTIC_ID), cris_client.ModelIdentity(ADAPTED_LANGUAGE_ID)]
    # )

    data, status, headers = transcription_api.create_transcription_with_http_info(transcription_definition)

    # extract transcription location from the headers
    transcription_location: str = headers["location"]

    # get the transcription Id from the location URI
    created_transcription: str = transcription_location.split('/')[-1]

    logging.info("Checking status.")

    completed = False
    running, not_started = 0, 0

    while not completed:
        # get all transcriptions for the user
        transcriptions: List[cris_client.Transcription] = transcription_api.get_transcriptions()

        # for each transcription in the list we check the status
        for transcription in transcriptions:
            if transcription.status == "Failed" or transcription.status == "Succeeded":
                # we check to see if it was one of the transcriptions we created from this client
                if created_transcription != transcription.id:
                    continue

                completed = True
                isTranscribing = False

                if transcription.status == "Succeeded":
                    results_uri = transcription.results_urls["channel_0"]
                    results = requests.get(results_uri)
                    logging.info("Transcription succeeded. Results: ")
                    #logging.info(results.content.decode("utf-8"))
                    jsonData = results.content.decode("utf-8")
                    data = json.loads(jsonData)

                    local_path=os.path.expanduser("~/Documents")
                    transcript_local_file_name = fileName + "-transcript.txt"
                    analysis_local_file_name = fileName + "-analysis.json"

                    transcript_full_path_to_file = os.path.join(local_path, transcript_local_file_name)
                    analysis_full_path_to_file = os.path.join(local_path, analysis_local_file_name)

                    file = open(transcript_full_path_to_file, 'w')
                    file.write(getTranscript(data))
                    file.close()

                    file = open(analysis_full_path_to_file, 'w')
                    file.write(jsonData)
                    file.close()

                    block_blob_service.create_blob_from_path(TRANSCRIPT_CONTAINER, transcript_local_file_name, transcript_full_path_to_file)
                    block_blob_service.create_blob_from_path(ANALYSIS_CONTAINER, analysis_local_file_name, analysis_full_path_to_file)

                    logging.info("\n\nFull Transcript:{}".format(getTranscript(data)))
                    logging.info("\n\nTranscript Metadata:{}".format(jsonData))
                    
            elif transcription.status == "Running":
                running += 1
            elif transcription.status == "NotStarted":
                not_started += 1
                if not_started > 6:
                    SUB_KEY_INDEX += 1
                    transcribe(fileName)

        logging.info("Transcriptions status: completed (this transcription): {}, {} running, {} not started yet".format(completed, running, not_started))
        if transcription.status == "Failed":
            SUB_KEY_INDEX += 1
            logging.info("Transcription failed. Retrying")
            transcribe(fileName)
        # wait for 5 seconds
        time.sleep(5)

def startPolling():
    block_blob_service = BlockBlobService(account_name='audiophilesdata', account_key='HNRhdcv4TVEp8mcgDc0B7GfbzS3RnCEuBgGr71auzhZkd7mkHu6aBpHU1TBoZb3YTnM0SDEsiEP6jO4i8Q0D5g==')

    generator = block_blob_service.list_blobs(AUDIO_CONTAINER)
    blob_names = [blob.name for blob in generator]
    print("Starting Files are: ")
    for name in blob_names:
        print("'" + name + "'")
    
    while True:
        generator = block_blob_service.list_blobs(AUDIO_CONTAINER)
        updated_blob_names = [blob.name for blob in generator]

        new_blob_names = diff(updated_blob_names, blob_names)
        if len(new_blob_names) > 0 and not isTranscribing:
            name = new_blob_names[0]
            print("Found a new file called " + name)
            blob_names.append(name)
            transcribe(name)
        else:
            print("Nothing new")
            blob_names = updated_blob_names

        time.sleep(5)

if __name__ == "__main__":
    startPolling()
    # if len(sys.argv) == 2:
    #     transcribe(sys.argv[1])
    # else:
    #     logging.info("USAGE 'python speechToText.py <AUDIO-FILE-NAME>'")
