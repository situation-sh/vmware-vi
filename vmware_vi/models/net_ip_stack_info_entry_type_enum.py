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


class NetIpStackInfoEntryTypeEnum(str, Enum):
    """
    IP Stack keeps state on entries in IpNetToMedia table to perform physical address lookups for IP addresses.  Here are the standard states per @see RFC 4293 ipNetToMediaType.  Possible values: - `other`: This implementation is reporting something other than   what states are listed below. - `invalid`: The IP Stack has marked this entry as not useable. - `dynamic`: This entry has been learned using ARP or NDP. - `manual`: This entry was set manually.    ***Since:*** vSphere API 4.1 
    """

    """
    allowed enum values
    """
    OTHER = 'other'
    INVALID = 'invalid'
    DYNAMIC = 'dynamic'
    MANUAL = 'manual'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NetIpStackInfoEntryTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


