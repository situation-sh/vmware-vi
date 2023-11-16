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


class PerformanceManagerUnitEnum(str, Enum):
    """
    Indicates the unit of measure represented by a counter or statistical value.  Possible values: - `percent`: Percentage values in units of 1/100th of a percent.      For example 100   represents 1%. - `kiloBytes`: Kilobytes. - `megaBytes`: Megabytes. - `megaHertz`: Megahertz. - `number`: A quantity of items, for example, the number of CPUs. - `microsecond`: The time in microseconds.      ***Since:*** vSphere API 4.0 - `millisecond`: The time in milliseconds. - `second`: The time in seconds. - `kiloBytesPerSecond`: Kilobytes per second. - `megaBytesPerSecond`: Megabytes per second. - `watt`: Watts      ***Since:*** vSphere API 4.1 - `joule`: Joules      ***Since:*** vSphere API 4.1 - `teraBytes`: Terabytes.      ***Since:*** vSphere API 6.0 - `celsius`: Temperature in celsius.      ***Since:*** vSphere API 6.5 - `mgCO2eqPerHour`: Milligram CO2 equivalent per hour.      ***Since:*** vim GreenMetrics version - `nanosecond`: The time in nanoseconds. 
    """

    """
    allowed enum values
    """
    PERCENT = 'percent'
    KILOBYTES = 'kiloBytes'
    MEGABYTES = 'megaBytes'
    MEGAHERTZ = 'megaHertz'
    NUMBER = 'number'
    MICROSECOND = 'microsecond'
    MILLISECOND = 'millisecond'
    SECOND = 'second'
    KILOBYTESPERSECOND = 'kiloBytesPerSecond'
    MEGABYTESPERSECOND = 'megaBytesPerSecond'
    WATT = 'watt'
    JOULE = 'joule'
    TERABYTES = 'teraBytes'
    CELSIUS = 'celsius'
    MGCO2EQPERHOUR = 'mgCO2eqPerHour'
    NANOSECOND = 'nanosecond'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PerformanceManagerUnitEnum from a JSON string"""
        return cls(json.loads(json_str))


