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


class RollingUpgradeRunningStatus(Model):
    """Information about the current running state of the overall upgrade.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: Code indicating the current status of the upgrade. Possible
     values include: 'RollingForward', 'Cancelled', 'Completed', 'Faulted'
    :vartype code: str or
     ~azure.mgmt.compute.v2017_03_30.models.RollingUpgradeStatusCode
    :ivar start_time: Start time of the upgrade.
    :vartype start_time: datetime
    :ivar last_action: The last action performed on the rolling upgrade.
     Possible values include: 'Start', 'Cancel'
    :vartype last_action: str or
     ~azure.mgmt.compute.v2017_03_30.models.RollingUpgradeActionType
    :ivar last_action_time: Last action time of the upgrade.
    :vartype last_action_time: datetime
    """

    _validation = {
        'code': {'readonly': True},
        'start_time': {'readonly': True},
        'last_action': {'readonly': True},
        'last_action_time': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'RollingUpgradeStatusCode'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'last_action': {'key': 'lastAction', 'type': 'RollingUpgradeActionType'},
        'last_action_time': {'key': 'lastActionTime', 'type': 'iso-8601'},
    }

    def __init__(self):
        super(RollingUpgradeRunningStatus, self).__init__()
        self.code = None
        self.start_time = None
        self.last_action = None
        self.last_action_time = None
