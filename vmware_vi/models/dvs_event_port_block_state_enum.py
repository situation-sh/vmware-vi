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


class DvsEventPortBlockStateEnum(str, Enum):
    """
    The port blocked/unblocked state.  Possible values: - `unset`: The dvs port is in unset state - `blocked`: The dvs port is in blocked state - `unblocked`: The dvs port is in unblocked state - `unknown`: The dvs port is in unknown state    ***Since:*** vSphere API 6.5 
    """

    """
    allowed enum values
    """
    UNSET = 'unset'
    BLOCKED = 'blocked'
    UNBLOCKED = 'unblocked'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DvsEventPortBlockStateEnum from a JSON string"""
        return cls(json.loads(json_str))


