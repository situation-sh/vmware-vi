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


class HostNumericSensorHealthStateEnum(str, Enum):
    """
    Health state of the numeric sensor as reported by the sensor probes.  Same data reported using command line: esxcli hardware ipmi sdr list  Possible values: - `unknown`: The implementation cannot report on the current health state of the   physical element - `green`: The sensor is operating under normal conditions - `yellow`: The sensor is operating under conditions that are non-critical. - `red`: The sensor is operating under critical or fatal conditions.      This may   directly affect the functioning of both the sensor and related   components.  ***Since:*** VI API 2.5 
    """

    """
    allowed enum values
    """
    UNKNOWN = 'unknown'
    GREEN = 'green'
    YELLOW = 'yellow'
    RED = 'red'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostNumericSensorHealthStateEnum from a JSON string"""
        return cls(json.loads(json_str))


