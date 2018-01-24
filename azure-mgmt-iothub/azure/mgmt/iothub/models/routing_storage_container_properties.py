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

from msrest.serialization import Model


class RoutingStorageContainerProperties(Model):
    """The properties related to a storage container endpoint.

    :param connection_string: The connection string of the storage account.
    :type connection_string: str
    :param name: The name that identifies this endpoint. The name can only
     include alphanumeric characters, periods, underscores, hyphens and has a
     maximum length of 64 characters. The following names are reserved:
     events, operationsMonitoringEvents, fileNotifications, $default. Endpoint
     names must be unique across endpoint types.
    :type name: str
    :param subscription_id: The subscription identifier of the storage
     account.
    :type subscription_id: str
    :param resource_group: The name of the resource group of the storage
     account.
    :type resource_group: str
    :param container_name: The name of storage container in the storage
     account.
    :type container_name: str
    :param file_name_format: File name format for the blob. Default format is
     {iothub}/{partition}/{YYYY}/{MM}/{DD}/{HH}/{mm}. All parameters are
     mandatory but can be reordered.
    :type file_name_format: str
    :param batch_frequency_in_seconds: Time interval at which blobs are
     written to storage. Value should be between 60 and 720 seconds. Default
     value is 300 seconds.
    :type batch_frequency_in_seconds: int
    :param max_chunk_size_in_bytes: Maximum number of bytes for each blob
     written to storage. Value should be between 10485760(10MB) and
     524288000(500MB). Default value is 314572800(300MB).
    :type max_chunk_size_in_bytes: int
    :param encoding: Encoding that is used to serialize messages to blobs.
     Supported values are 'avro' and 'avrodeflate'. Default value is 'avro'.
    :type encoding: str
    """

    _validation = {
        'connection_string': {'required': True},
        'name': {'required': True, 'pattern': r'^[A-Za-z0-9-._]{1,64}$'},
        'container_name': {'required': True},
        'batch_frequency_in_seconds': {'maximum': 720, 'minimum': 60},
        'max_chunk_size_in_bytes': {'maximum': 524288000, 'minimum': 10485760},
    }

    _attribute_map = {
        'connection_string': {'key': 'connectionString', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'resource_group': {'key': 'resourceGroup', 'type': 'str'},
        'container_name': {'key': 'containerName', 'type': 'str'},
        'file_name_format': {'key': 'fileNameFormat', 'type': 'str'},
        'batch_frequency_in_seconds': {'key': 'batchFrequencyInSeconds', 'type': 'int'},
        'max_chunk_size_in_bytes': {'key': 'maxChunkSizeInBytes', 'type': 'int'},
        'encoding': {'key': 'encoding', 'type': 'str'},
    }

    def __init__(self, connection_string, name, container_name, subscription_id=None, resource_group=None, file_name_format=None, batch_frequency_in_seconds=None, max_chunk_size_in_bytes=None, encoding=None):
        self.connection_string = connection_string
        self.name = name
        self.subscription_id = subscription_id
        self.resource_group = resource_group
        self.container_name = container_name
        self.file_name_format = file_name_format
        self.batch_frequency_in_seconds = batch_frequency_in_seconds
        self.max_chunk_size_in_bytes = max_chunk_size_in_bytes
        self.encoding = encoding
