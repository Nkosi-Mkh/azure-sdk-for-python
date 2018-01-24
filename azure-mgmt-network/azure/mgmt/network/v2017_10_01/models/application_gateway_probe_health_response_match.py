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


class ApplicationGatewayProbeHealthResponseMatch(Model):
    """Application gateway probe health response match.

    :param body: Body that must be contained in the health response. Default
     value is empty.
    :type body: str
    :param status_codes: Allowed ranges of healthy status codes. Default range
     of healthy status codes is 200-399.
    :type status_codes: list[str]
    """

    _attribute_map = {
        'body': {'key': 'body', 'type': 'str'},
        'status_codes': {'key': 'statusCodes', 'type': '[str]'},
    }

    def __init__(self, body=None, status_codes=None):
        super(ApplicationGatewayProbeHealthResponseMatch, self).__init__()
        self.body = body
        self.status_codes = status_codes
