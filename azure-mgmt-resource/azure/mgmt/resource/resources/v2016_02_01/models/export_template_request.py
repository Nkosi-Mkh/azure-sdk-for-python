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


class ExportTemplateRequest(Model):
    """Export resource group template request parameters.

    :param resources: The ids of the resources. The only supported string
     currently is '*' (all resources). Future api updates will support
     exporting specific resources.
    :type resources: list[str]
    :param options: The export template options. Supported values include
     'IncludeParameterDefaultValue', 'IncludeComments' or
     'IncludeParameterDefaultValue, IncludeComments
    :type options: str
    """

    _attribute_map = {
        'resources': {'key': 'resources', 'type': '[str]'},
        'options': {'key': 'options', 'type': 'str'},
    }

    def __init__(self, resources=None, options=None):
        self.resources = resources
        self.options = options
