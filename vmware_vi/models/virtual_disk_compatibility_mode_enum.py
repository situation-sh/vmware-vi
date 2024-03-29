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


class VirtualDiskCompatibilityModeEnum(str, Enum):
    """
    All known compatibility modes for raw disk mappings.  Valid compatibility modes are: - virtualMode - physicalMode    Possible values: - `virtualMode`: A disk device backed by a virtual compatibility mode raw disk mapping can   use disk modes.      See also *VirtualDiskMode_enum*. - `physicalMode`: A disk device backed by a physical compatibility mode raw disk mapping cannot   use disk modes, and commands are passed straight through to the LUN   indicated by the raw disk mapping. 
    """

    """
    allowed enum values
    """
    VIRTUALMODE = 'virtualMode'
    PHYSICALMODE = 'physicalMode'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualDiskCompatibilityModeEnum from a JSON string"""
        return cls(json.loads(json_str))


