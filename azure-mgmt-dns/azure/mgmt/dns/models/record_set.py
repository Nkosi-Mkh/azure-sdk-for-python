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


class RecordSet(Model):
    """Describes a DNS record set (a collection of DNS records with the same name
    and type).

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The ID of the record set.
    :vartype id: str
    :ivar name: The name of the record set.
    :vartype name: str
    :ivar type: The type of the record set.
    :vartype type: str
    :param etag: The etag of the record set.
    :type etag: str
    :param metadata: The metadata attached to the record set.
    :type metadata: dict[str, str]
    :param ttl: The TTL (time-to-live) of the records in the record set.
    :type ttl: long
    :ivar fqdn: Fully qualified domain name of the record set.
    :vartype fqdn: str
    :param arecords: The list of A records in the record set.
    :type arecords: list[~azure.mgmt.dns.models.ARecord]
    :param aaaa_records: The list of AAAA records in the record set.
    :type aaaa_records: list[~azure.mgmt.dns.models.AaaaRecord]
    :param mx_records: The list of MX records in the record set.
    :type mx_records: list[~azure.mgmt.dns.models.MxRecord]
    :param ns_records: The list of NS records in the record set.
    :type ns_records: list[~azure.mgmt.dns.models.NsRecord]
    :param ptr_records: The list of PTR records in the record set.
    :type ptr_records: list[~azure.mgmt.dns.models.PtrRecord]
    :param srv_records: The list of SRV records in the record set.
    :type srv_records: list[~azure.mgmt.dns.models.SrvRecord]
    :param txt_records: The list of TXT records in the record set.
    :type txt_records: list[~azure.mgmt.dns.models.TxtRecord]
    :param cname_record: The CNAME record in the  record set.
    :type cname_record: ~azure.mgmt.dns.models.CnameRecord
    :param soa_record: The SOA record in the record set.
    :type soa_record: ~azure.mgmt.dns.models.SoaRecord
    :param caa_records: The list of CAA records in the record set.
    :type caa_records: list[~azure.mgmt.dns.models.CaaRecord]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'fqdn': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': '{str}'},
        'ttl': {'key': 'properties.TTL', 'type': 'long'},
        'fqdn': {'key': 'properties.fqdn', 'type': 'str'},
        'arecords': {'key': 'properties.ARecords', 'type': '[ARecord]'},
        'aaaa_records': {'key': 'properties.AAAARecords', 'type': '[AaaaRecord]'},
        'mx_records': {'key': 'properties.MXRecords', 'type': '[MxRecord]'},
        'ns_records': {'key': 'properties.NSRecords', 'type': '[NsRecord]'},
        'ptr_records': {'key': 'properties.PTRRecords', 'type': '[PtrRecord]'},
        'srv_records': {'key': 'properties.SRVRecords', 'type': '[SrvRecord]'},
        'txt_records': {'key': 'properties.TXTRecords', 'type': '[TxtRecord]'},
        'cname_record': {'key': 'properties.CNAMERecord', 'type': 'CnameRecord'},
        'soa_record': {'key': 'properties.SOARecord', 'type': 'SoaRecord'},
        'caa_records': {'key': 'properties.caaRecords', 'type': '[CaaRecord]'},
    }

    def __init__(self, etag=None, metadata=None, ttl=None, arecords=None, aaaa_records=None, mx_records=None, ns_records=None, ptr_records=None, srv_records=None, txt_records=None, cname_record=None, soa_record=None, caa_records=None):
        self.id = None
        self.name = None
        self.type = None
        self.etag = etag
        self.metadata = metadata
        self.ttl = ttl
        self.fqdn = None
        self.arecords = arecords
        self.aaaa_records = aaaa_records
        self.mx_records = mx_records
        self.ns_records = ns_records
        self.ptr_records = ptr_records
        self.srv_records = srv_records
        self.txt_records = txt_records
        self.cname_record = cname_record
        self.soa_record = soa_record
        self.caa_records = caa_records
