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


class ManagedEntityStatusEnum(str, Enum):
    """
    The Status enumeration defines a general \"health\" value for a managed entity.  Possible values: - `gray`: The status is unknown. - `green`: The entity is OK. - `yellow`: The entity might have a problem. - `red`: The entity definitely has a problem. 
    """

    """
    allowed enum values
    """
    GRAY = 'gray'
    GREEN = 'green'
    YELLOW = 'yellow'
    RED = 'red'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ManagedEntityStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


