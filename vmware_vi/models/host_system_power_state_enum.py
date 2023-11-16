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


class HostSystemPowerStateEnum(str, Enum):
    """
    Defines a host's power state.  Possible values: - `poweredOn`: The host is powered on.      A host that is entering standby mode   *entering* is also in this state. - `poweredOff`: The host was specifically powered off by the user through   VirtualCenter.      This state is not a cetain state, because   after VirtualCenter issues the command to power off the host,   the host might crash, or kill all the processes but fail to   power off. - `standBy`: The host was specifically put in standby mode, either   explicitly by the user, or automatically by DPM.      This state   is not a cetain state, because after VirtualCenter issues the   command to put the host in standby state, the host might   crash, or kill all the processes but fail to power off. A host   that is exiting standby mode *exiting*   is also in this state. - `unknown`: If the host is disconnected, or notResponding, we cannot   possibly have knowledge of its power state.      Hence, the host   is marked as unknown.  ***Since:*** VI API 2.5 
    """

    """
    allowed enum values
    """
    POWEREDON = 'poweredOn'
    POWEREDOFF = 'poweredOff'
    STANDBY = 'standBy'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostSystemPowerStateEnum from a JSON string"""
        return cls(json.loads(json_str))

