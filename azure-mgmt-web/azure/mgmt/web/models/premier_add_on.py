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

from .resource import Resource


class PremierAddOn(Resource):
    """Premier add-on.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :param location: Resource Location.
    :type location: str
    :ivar type: Resource type.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param sku: SKU.
    :type sku: str
    :param product: Product.
    :type product: str
    :param vendor: Vendor.
    :type vendor: str
    :param premier_add_on_name: Name.
    :type premier_add_on_name: str
    :param premier_add_on_location: Location.
    :type premier_add_on_location: str
    :param premier_add_on_tags: Tags.
    :type premier_add_on_tags: dict[str, str]
    :param marketplace_publisher: Marketplace publisher.
    :type marketplace_publisher: str
    :param marketplace_offer: Marketplace offer.
    :type marketplace_offer: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'location': {'required': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'properties.sku', 'type': 'str'},
        'product': {'key': 'properties.product', 'type': 'str'},
        'vendor': {'key': 'properties.vendor', 'type': 'str'},
        'premier_add_on_name': {'key': 'properties.name', 'type': 'str'},
        'premier_add_on_location': {'key': 'properties.location', 'type': 'str'},
        'premier_add_on_tags': {'key': 'properties.tags', 'type': '{str}'},
        'marketplace_publisher': {'key': 'properties.marketplacePublisher', 'type': 'str'},
        'marketplace_offer': {'key': 'properties.marketplaceOffer', 'type': 'str'},
    }

    def __init__(self, location, kind=None, tags=None, sku=None, product=None, vendor=None, premier_add_on_name=None, premier_add_on_location=None, premier_add_on_tags=None, marketplace_publisher=None, marketplace_offer=None):
        super(PremierAddOn, self).__init__(kind=kind, location=location, tags=tags)
        self.sku = sku
        self.product = product
        self.vendor = vendor
        self.premier_add_on_name = premier_add_on_name
        self.premier_add_on_location = premier_add_on_location
        self.premier_add_on_tags = premier_add_on_tags
        self.marketplace_publisher = marketplace_publisher
        self.marketplace_offer = marketplace_offer
