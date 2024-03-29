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


class VirtualDiskDeltaDiskFormatEnum(str, Enum):
    """
    The delta disk format constants  Possible values: - `redoLogFormat`: redo-log based format - `nativeFormat`: native snapshot format - `seSparseFormat`: Flex-SE redo-log based format      ***Since:*** vSphere API 5.1  ***Since:*** vSphere API 5.0 
    """

    """
    allowed enum values
    """
    REDOLOGFORMAT = 'redoLogFormat'
    NATIVEFORMAT = 'nativeFormat'
    SESPARSEFORMAT = 'seSparseFormat'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualDiskDeltaDiskFormatEnum from a JSON string"""
        return cls(json.loads(json_str))


