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


class HostDiskPartitionInfoTypeEnum(str, Enum):
    """
    List of symbol partition types  Possible values: - `none` - `vmfs` - `linuxNative` - `linuxSwap` - `extended` - `ntfs` - `vmkDiagnostic` - `vffs`: ***Since:*** vSphere API 5.5 
    """

    """
    allowed enum values
    """
    NONE = 'none'
    VMFS = 'vmfs'
    LINUXNATIVE = 'linuxNative'
    LINUXSWAP = 'linuxSwap'
    EXTENDED = 'extended'
    NTFS = 'ntfs'
    VMKDIAGNOSTIC = 'vmkDiagnostic'
    VFFS = 'vffs'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostDiskPartitionInfoTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


