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


class PerfSummaryTypeEnum(str, Enum):
    """
    Indicates how multiple samples of a specific counter type are transformed into a single statistical value.  Possible values: - `average`: The actual value collected or the average of all values collected   during the summary period. - `maximum`: The maximum value of the performance counter value over the   summarization period. - `minimum`: The minimum value of the performance counter value over the   summarization period. - `latest`: The most recent value of the performance counter over the   summarization period. - `summation`: The sum of all the values of the performance counter over the   summarization period. - `none`: The counter is never rolled up. 
    """

    """
    allowed enum values
    """
    AVERAGE = 'average'
    MAXIMUM = 'maximum'
    MINIMUM = 'minimum'
    LATEST = 'latest'
    SUMMATION = 'summation'
    NONE = 'none'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PerfSummaryTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


