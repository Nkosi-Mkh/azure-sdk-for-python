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


class ContractualRulesContractualRule(Model):
    """ContractualRulesContractualRule.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ContractualRulesAttribution

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar target_property_name: The name of the field that the rule applies
     to.
    :vartype target_property_name: str
    :param _type: Constant filled by server.
    :type _type: str
    """

    _validation = {
        'target_property_name': {'readonly': True},
        '_type': {'required': True},
    }

    _attribute_map = {
        'target_property_name': {'key': 'targetPropertyName', 'type': 'str'},
        '_type': {'key': '_type', 'type': 'str'},
    }

    _subtype_map = {
        '_type': {'ContractualRules/Attribution': 'ContractualRulesAttribution'}
    }

    def __init__(self):
        super(ContractualRulesContractualRule, self).__init__()
        self.target_property_name = None
        self._type = None
