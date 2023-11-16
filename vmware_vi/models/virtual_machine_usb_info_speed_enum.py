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


class VirtualMachineUsbInfoSpeedEnum(str, Enum):
    """
    Device speed.  Possible values: - `low`: This device operates at low speed (1.5Mb/s). - `full`: This device operates at full speed (12Mb/s). - `high`: This device can operate at high speed (480Mb/s) - `superSpeed`: This device can operate at super speed (4.8Gb/s)      ***Since:*** vSphere API 5.0 - `superSpeedPlus`: This device can operate at super speed plus (10Gb/s)      ***Since:*** vSphere API 6.8.7 - `superSpeed20Gbps`: This device can operate at super speed gen 2x2 (20Gb/s) - `unknownSpeed`: This device's speed is unknown.    ***Since:*** VI API 2.5 
    """

    """
    allowed enum values
    """
    LOW = 'low'
    FULL = 'full'
    HIGH = 'high'
    SUPERSPEED = 'superSpeed'
    SUPERSPEEDPLUS = 'superSpeedPlus'
    SUPERSPEED20GBPS = 'superSpeed20Gbps'
    UNKNOWNSPEED = 'unknownSpeed'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualMachineUsbInfoSpeedEnum from a JSON string"""
        return cls(json.loads(json_str))


