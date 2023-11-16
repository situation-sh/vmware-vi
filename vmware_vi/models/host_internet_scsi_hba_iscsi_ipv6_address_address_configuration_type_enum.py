# coding: utf-8

"""
    Virtual Infrastructure JSON API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 8.0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class HostInternetScsiHbaIscsiIpv6AddressAddressConfigurationTypeEnum(str, Enum):
    """
    enum listing possible IPv6 address configuration methods.  Possible values: - `DHCP`: DHCP - `AutoConfigured`: Auto configured.      Auto configured Link local address and Router Advertisement addresses   would be of this type. - `Static`: Static address.      Typically user specified addresses will be static addresses.   User can specify link local address. Only Static addresses can be added or removed. - `Other`: Other or unknown type.    ***Since:*** vSphere API 6.0 
    """

    """
    allowed enum values
    """
    DHCP = 'DHCP'
    AUTOCONFIGURED = 'AutoConfigured'
    STATIC = 'Static'
    OTHER = 'Other'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostInternetScsiHbaIscsiIpv6AddressAddressConfigurationTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


