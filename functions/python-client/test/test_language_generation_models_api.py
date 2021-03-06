# coding: utf-8

"""
    Speech Services API v2.0

    Speech Services API v2.0.  # noqa: E501

    OpenAPI spec version: v2.0
    Contact: crservice@microsoft.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.language_generation_models_api import LanguageGenerationModelsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestLanguageGenerationModelsApi(unittest.TestCase):
    """LanguageGenerationModelsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.language_generation_models_api.LanguageGenerationModelsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_language_generation_model(self):
        """Test case for create_language_generation_model

        Creates a new language generation model.  # noqa: E501
        """
        pass

    def test_delete_language_generation_model(self):
        """Test case for delete_language_generation_model

        Deletes the language generation model with the given id.  # noqa: E501
        """
        pass

    def test_get_language_generation_model(self):
        """Test case for get_language_generation_model

        Gets the specified language generation model.  # noqa: E501
        """
        pass

    def test_get_language_generation_models(self):
        """Test case for get_language_generation_models

        Gets all language generation model of a subscription.  # noqa: E501
        """
        pass

    def test_get_supported_locales_for_language_generation_models(self):
        """Test case for get_supported_locales_for_language_generation_models

        Gets a list of supported locales for language generation model creation.  # noqa: E501
        """
        pass

    def test_update_language_generation_model(self):
        """Test case for update_language_generation_model

        Updates the mutable details of the language generation model identified by its id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
