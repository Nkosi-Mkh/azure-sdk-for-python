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


class TypeFieldInfo(Model):
    """A Data Lake Analytics catalog type field information item.

    :param name: the name of the field associated with this type.
    :type name: str
    :param type: the type of the field.
    :type type: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, name=None, type=None):
        super(TypeFieldInfo, self).__init__()
        self.name = name
        self.type = type
