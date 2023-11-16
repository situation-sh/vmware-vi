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


class VirtualMachineFlagInfoVirtualExecUsageEnum(str, Enum):
    """
    Set of possible values for *VirtualMachineFlagInfo.virtualExecUsage*.  Possible values: - `hvAuto`: Determine automatically whether to use hardware virtualization (HV) support. - `hvOn`: Use hardware virtualization (HV) support if the physical hardware supports it. - `hvOff`: Do not use hardware virtualization (HV) support.    ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    HVAUTO = 'hvAuto'
    HVON = 'hvOn'
    HVOFF = 'hvOff'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualMachineFlagInfoVirtualExecUsageEnum from a JSON string"""
        return cls(json.loads(json_str))

