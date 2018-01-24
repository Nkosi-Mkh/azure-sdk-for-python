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

from .proxy_resource import ProxyResource


class DataMaskingPolicy(ProxyResource):
    """Represents a database data masking policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param data_masking_state: The state of the data masking policy. Possible
     values include: 'Disabled', 'Enabled'
    :type data_masking_state: str or ~azure.mgmt.sql.models.DataMaskingState
    :param exempt_principals: The list of the exempt principals. Specifies the
     semicolon-separated list of database users for which the data masking
     policy does not apply. The specified users receive data results without
     masking for all of the database queries.
    :type exempt_principals: str
    :ivar application_principals: The list of the application principals. This
     is a legacy parameter and is no longer used.
    :vartype application_principals: str
    :ivar masking_level: The masking level. This is a legacy parameter and is
     no longer used.
    :vartype masking_level: str
    :ivar location: The location of the data masking policy.
    :vartype location: str
    :ivar kind: The kind of data masking policy. Metadata, used for Azure
     portal.
    :vartype kind: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'data_masking_state': {'required': True},
        'application_principals': {'readonly': True},
        'masking_level': {'readonly': True},
        'location': {'readonly': True},
        'kind': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'data_masking_state': {'key': 'properties.dataMaskingState', 'type': 'DataMaskingState'},
        'exempt_principals': {'key': 'properties.exemptPrincipals', 'type': 'str'},
        'application_principals': {'key': 'properties.applicationPrincipals', 'type': 'str'},
        'masking_level': {'key': 'properties.maskingLevel', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, data_masking_state, exempt_principals=None):
        super(DataMaskingPolicy, self).__init__()
        self.data_masking_state = data_masking_state
        self.exempt_principals = exempt_principals
        self.application_principals = None
        self.masking_level = None
        self.location = None
        self.kind = None
