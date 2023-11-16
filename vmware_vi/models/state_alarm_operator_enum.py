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


class StateAlarmOperatorEnum(str, Enum):
    """
    The operation on the target state.  Possible values: - `isEqual`: Test if the target state matches the given red or yellow states. - `isUnequal`: Test if the target state does not match the given red or yellow states. 
    """

    """
    allowed enum values
    """
    ISEQUAL = 'isEqual'
    ISUNEQUAL = 'isUnequal'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StateAlarmOperatorEnum from a JSON string"""
        return cls(json.loads(json_str))


