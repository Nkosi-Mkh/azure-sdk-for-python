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


class Accessory(Model):
    """Accessory item and corresponding confidence level.

    :param type: Type of an accessory. Possible values include: 'headWear',
     'glasses', 'mask'
    :type type: str or
     ~azure.cognitiveservices.vision.face.models.AccessoryType
    :param confidence: Confidence level of an accessory
    :type confidence: float
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'AccessoryType'},
        'confidence': {'key': 'confidence', 'type': 'float'},
    }

    def __init__(self, type=None, confidence=None):
        super(Accessory, self).__init__()
        self.type = type
        self.confidence = confidence
