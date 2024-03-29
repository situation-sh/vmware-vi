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


class HostOpaqueSwitchOpaqueSwitchStateEnum(str, Enum):
    """
    Possible values: - `up`: The opaque switch is up and running. - `warning`: The opaque switch requires attention. - `down`: The opaque switch is down. - `maintenance`: The opaque switch is under upgrade.      ***Since:*** vSphere API 7.0  ***Since:*** vSphere API 6.0 
    """

    """
    allowed enum values
    """
    UP = 'up'
    WARNING = 'warning'
    DOWN = 'down'
    MAINTENANCE = 'maintenance'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostOpaqueSwitchOpaqueSwitchStateEnum from a JSON string"""
        return cls(json.loads(json_str))


