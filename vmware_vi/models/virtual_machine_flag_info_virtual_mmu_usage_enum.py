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


class VirtualMachineFlagInfoVirtualMmuUsageEnum(str, Enum):
    """
    Set of possible values for *VirtualMachineFlagInfo.virtualMmuUsage*.  Possible values: - `automatic`: Determine automatically whether to use nested page table hardware support. - `on`: Use nested paging hardware support if the physical hardware supports it. - `off`: Do not use nested page table hardware support.    ***Since:*** VI API 2.5 
    """

    """
    allowed enum values
    """
    AUTOMATIC = 'automatic'
    TRUE = 'true'
    FALSE = 'false'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualMachineFlagInfoVirtualMmuUsageEnum from a JSON string"""
        return cls(json.loads(json_str))

