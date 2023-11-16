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


class VirtualDiskSharingEnum(str, Enum):
    """
    The sharing mode of the virtual disk.  Setting the value to sharingMultiWriter means that multiple virtual machines can write to the virtual disk. This sharing mode is allowed only for eagerly zeroed thick virtual disks.  Possible values: - `sharingNone`: The virtual disk is not shared. - `sharingMultiWriter`: The virtual disk is shared between multiple virtual machines.    ***Since:*** vSphere API 6.0 
    """

    """
    allowed enum values
    """
    SHARINGNONE = 'sharingNone'
    SHARINGMULTIWRITER = 'sharingMultiWriter'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualDiskSharingEnum from a JSON string"""
        return cls(json.loads(json_str))


