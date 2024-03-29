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


class VirtualEthernetCardLegacyNetworkDeviceNameEnum(str, Enum):
    """
    Possible device names for legacy network backing option are listed below.  Note: This is not an exhaustive list. It is possible to specify a specific device as well. For example, on ESX hosts, the device name could be specified as \"vmnic\\[0-9\\]\" or vmnet\\_\\[0-9\\]. For VMware Server Windows hosts, the device name could be specified as \"vmnet\\[0-9\\]\" and for VMware Server Linux hosts, the device name could be specified as \"/dev/vmnet\\[0-9\\]\" depending on what devices are available on that particular host.  Possible values: - `bridged` - `nat` - `hostonly` 
    """

    """
    allowed enum values
    """
    BRIDGED = 'bridged'
    NAT = 'nat'
    HOSTONLY = 'hostonly'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualEthernetCardLegacyNetworkDeviceNameEnum from a JSON string"""
        return cls(json.loads(json_str))


