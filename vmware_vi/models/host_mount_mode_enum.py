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


class HostMountModeEnum(str, Enum):
    """
    Defines the access mode of the datastore.  Possible values: - `readWrite`: The host system has read/write access to the file system. - `readOnly`: The host system has read-only access to the file system. 
    """

    """
    allowed enum values
    """
    READWRITE = 'readWrite'
    READONLY = 'readOnly'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostMountModeEnum from a JSON string"""
        return cls(json.loads(json_str))


