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


class VirtualMachineStandbyActionTypeEnum(str, Enum):
    """
    The list of possible standby actions that the virtual machine can take for S1 ACPI.  Possible values: - `checkpoint` - `powerOnSuspend` 
    """

    """
    allowed enum values
    """
    CHECKPOINT = 'checkpoint'
    POWERONSUSPEND = 'powerOnSuspend'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualMachineStandbyActionTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


