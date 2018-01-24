# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.custom_instance_operations import CustomInstanceOperations
from . import models


class CustomSearchAPIConfiguration(Configuration):
    """Configuration for CustomSearchAPI
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://api.cognitive.microsoft.com/bingcustomsearch/v7.0'

        super(CustomSearchAPIConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-cognitiveservices-search-customsearch/{}'.format(VERSION))

        self.credentials = credentials


class CustomSearchAPI(object):
    """The Bing Custom Search API lets you send a search query to Bing and get back search results customized to meet your custom search definition.

    :ivar config: Configuration for client.
    :vartype config: CustomSearchAPIConfiguration

    :ivar custom_instance: CustomInstance operations
    :vartype custom_instance: azure.cognitiveservices.search.customsearch.operations.CustomInstanceOperations

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = CustomSearchAPIConfiguration(credentials, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.custom_instance = CustomInstanceOperations(
            self._client, self.config, self._serialize, self._deserialize)
