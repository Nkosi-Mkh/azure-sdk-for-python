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


class DatabaseAccountRegenerateKeyParameters(Model):
    """Parameters to regenerate the keys within the database account.

    :param key_kind: The access key to regenerate. Possible values include:
     'primary', 'secondary', 'primaryReadonly', 'secondaryReadonly'
    :type key_kind: str or ~azure.mgmt.cosmosdb.models.KeyKind
    """

    _validation = {
        'key_kind': {'required': True},
    }

    _attribute_map = {
        'key_kind': {'key': 'keyKind', 'type': 'str'},
    }

    def __init__(self, key_kind):
        self.key_kind = key_kind
