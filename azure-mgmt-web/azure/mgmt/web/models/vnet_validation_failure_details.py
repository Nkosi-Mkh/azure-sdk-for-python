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

from .proxy_only_resource import ProxyOnlyResource


class VnetValidationFailureDetails(ProxyOnlyResource):
    """A class that describes the reason for a validation failure.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param failed: A flag describing whether or not validation failed.
    :type failed: bool
    :param failed_tests: A list of tests that failed in the validation.
    :type failed_tests: list[~azure.mgmt.web.models.VnetValidationTestFailure]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'failed': {'key': 'properties.failed', 'type': 'bool'},
        'failed_tests': {'key': 'properties.failedTests', 'type': '[VnetValidationTestFailure]'},
    }

    def __init__(self, kind=None, failed=None, failed_tests=None):
        super(VnetValidationFailureDetails, self).__init__(kind=kind)
        self.failed = failed
        self.failed_tests = failed_tests
