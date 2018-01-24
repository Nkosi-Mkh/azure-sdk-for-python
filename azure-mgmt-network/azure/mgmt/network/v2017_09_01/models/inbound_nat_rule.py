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

from .sub_resource import SubResource


class InboundNatRule(SubResource):
    """Inbound NAT rule of the load balancer.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :param frontend_ip_configuration: A reference to frontend IP addresses.
    :type frontend_ip_configuration:
     ~azure.mgmt.network.v2017_09_01.models.SubResource
    :ivar backend_ip_configuration: A reference to a private IP address
     defined on a network interface of a VM. Traffic sent to the frontend port
     of each of the frontend IP configurations is forwarded to the backend IP.
    :vartype backend_ip_configuration:
     ~azure.mgmt.network.v2017_09_01.models.NetworkInterfaceIPConfiguration
    :param protocol: Possible values include: 'Udp', 'Tcp', 'All'
    :type protocol: str or
     ~azure.mgmt.network.v2017_09_01.models.TransportProtocol
    :param frontend_port: The port for the external endpoint. Port numbers for
     each rule must be unique within the Load Balancer. Acceptable values range
     from 1 to 65534.
    :type frontend_port: int
    :param backend_port: The port used for the internal endpoint. Acceptable
     values range from 1 to 65535.
    :type backend_port: int
    :param idle_timeout_in_minutes: The timeout for the TCP idle connection.
     The value can be set between 4 and 30 minutes. The default value is 4
     minutes. This element is only used when the protocol is set to TCP.
    :type idle_timeout_in_minutes: int
    :param enable_floating_ip: Configures a virtual machine's endpoint for the
     floating IP capability required to configure a SQL AlwaysOn Availability
     Group. This setting is required when using the SQL AlwaysOn Availability
     Groups in SQL server. This setting can't be changed after you create the
     endpoint.
    :type enable_floating_ip: bool
    :param provisioning_state: Gets the provisioning state of the public IP
     resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    """

    _validation = {
        'backend_ip_configuration': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'frontend_ip_configuration': {'key': 'properties.frontendIPConfiguration', 'type': 'SubResource'},
        'backend_ip_configuration': {'key': 'properties.backendIPConfiguration', 'type': 'NetworkInterfaceIPConfiguration'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'frontend_port': {'key': 'properties.frontendPort', 'type': 'int'},
        'backend_port': {'key': 'properties.backendPort', 'type': 'int'},
        'idle_timeout_in_minutes': {'key': 'properties.idleTimeoutInMinutes', 'type': 'int'},
        'enable_floating_ip': {'key': 'properties.enableFloatingIP', 'type': 'bool'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, frontend_ip_configuration=None, protocol=None, frontend_port=None, backend_port=None, idle_timeout_in_minutes=None, enable_floating_ip=None, provisioning_state=None, name=None, etag=None):
        super(InboundNatRule, self).__init__(id=id)
        self.frontend_ip_configuration = frontend_ip_configuration
        self.backend_ip_configuration = None
        self.protocol = protocol
        self.frontend_port = frontend_port
        self.backend_port = backend_port
        self.idle_timeout_in_minutes = idle_timeout_in_minutes
        self.enable_floating_ip = enable_floating_ip
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
