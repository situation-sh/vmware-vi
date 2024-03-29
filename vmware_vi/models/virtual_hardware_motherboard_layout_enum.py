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


class VirtualHardwareMotherboardLayoutEnum(str, Enum):
    """
    Motherboard layout of the VM.  Possible values: - `i440bxHostBridge`: Single i440BX host bridge. - `acpiHostBridges`: Multiple ACPI host bridges. 
    """

    """
    allowed enum values
    """
    I440BXHOSTBRIDGE = 'i440bxHostBridge'
    ACPIHOSTBRIDGES = 'acpiHostBridges'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualHardwareMotherboardLayoutEnum from a JSON string"""
        return cls(json.loads(json_str))


