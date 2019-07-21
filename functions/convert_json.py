import json

with open("result.unordered.json") as data_file:
    data = json.load(data_file)
    #print(data)

def getOffset(elem):
    return elem["Offset"]

def getTranscript(data):
    for num in data['AudioFileResults']:
        for segment in sorted(num['SegmentResults'], key = lambda i: i['Offset']):
            for nBest in segment['NBest']:
                print(nBest['Display'])

getTranscript(data)
#print(data['AudioFileResults'])