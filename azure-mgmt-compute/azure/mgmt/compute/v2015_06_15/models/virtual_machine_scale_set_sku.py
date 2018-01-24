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


class VirtualMachineScaleSetSku(Model):
    """Describes an available virtual machine scale set sku.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar resource_type: The type of resource the sku applies to.
    :vartype resource_type: str
    :ivar sku: The Sku.
    :vartype sku: ~azure.mgmt.compute.v2015_06_15.models.Sku
    :ivar capacity: Specifies the number of virtual machines in the scale set.
    :vartype capacity:
     ~azure.mgmt.compute.v2015_06_15.models.VirtualMachineScaleSetSkuCapacity
    """

    _validation = {
        'resource_type': {'readonly': True},
        'sku': {'readonly': True},
        'capacity': {'readonly': True},
    }

    _attribute_map = {
        'resource_type': {'key': 'resourceType', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'capacity': {'key': 'capacity', 'type': 'VirtualMachineScaleSetSkuCapacity'},
    }

    def __init__(self):
        super(VirtualMachineScaleSetSku, self).__init__()
        self.resource_type = None
        self.sku = None
        self.capacity = None
