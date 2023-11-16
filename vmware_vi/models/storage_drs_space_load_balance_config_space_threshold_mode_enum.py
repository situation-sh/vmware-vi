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


class StorageDrsSpaceLoadBalanceConfigSpaceThresholdModeEnum(str, Enum):
    """
    Defines the two ways a space utilization threshold can be specified.  Possible values: - `utilization`: Default mode: threshold as a percentage of datastore capacity - `freeSpace`: Threshold as an absolute value of free space in GBs    ***Since:*** vSphere API 6.0 
    """

    """
    allowed enum values
    """
    UTILIZATION = 'utilization'
    FREESPACE = 'freeSpace'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StorageDrsSpaceLoadBalanceConfigSpaceThresholdModeEnum from a JSON string"""
        return cls(json.loads(json_str))


