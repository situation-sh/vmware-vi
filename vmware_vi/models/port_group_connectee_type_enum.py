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


class PortGroupConnecteeTypeEnum(str, Enum):
    """
    The type of component connected to a port group.  Possible values: - `virtualMachine`: A virtual machine is connected to this port group. - `systemManagement`: A system management entity (service console)   is connected to this port group. - `host`: The VMkernel is connected to this port group. - `unknown`: This port group serves an entity of unspecified kind. 
    """

    """
    allowed enum values
    """
    VIRTUALMACHINE = 'virtualMachine'
    SYSTEMMANAGEMENT = 'systemManagement'
    HOST = 'host'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PortGroupConnecteeTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


