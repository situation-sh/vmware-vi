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


class VirtualAppVAppStateEnum(str, Enum):
    """
    The VAppState type defines the set of states a vApp can be in.  The transitory states between started and stopped is modeled explicitly, since the starting or stopping of a vApp is typically a time-consuming process that might take minutes to complete.  Possible values: - `started`: The vApp is currently powered on . - `stopped`: The vApp is currently powered off or suspended. - `starting`: The vApp is in the process of starting. - `stopping`: The vApp is in the process of stopping.    ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    STARTED = 'started'
    STOPPED = 'stopped'
    STARTING = 'starting'
    STOPPING = 'stopping'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualAppVAppStateEnum from a JSON string"""
        return cls(json.loads(json_str))


