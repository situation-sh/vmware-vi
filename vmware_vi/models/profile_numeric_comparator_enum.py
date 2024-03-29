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


class ProfileNumericComparatorEnum(str, Enum):
    """
    Enumerates different operations supported for comparing numerical values.  Possible values: - `lessThan` - `lessThanEqual` - `equal` - `notEqual` - `greaterThanEqual` - `greaterThan`  ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    LESSTHAN = 'lessThan'
    LESSTHANEQUAL = 'lessThanEqual'
    EQUAL = 'equal'
    NOTEQUAL = 'notEqual'
    GREATERTHANEQUAL = 'greaterThanEqual'
    GREATERTHAN = 'greaterThan'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProfileNumericComparatorEnum from a JSON string"""
        return cls(json.loads(json_str))


