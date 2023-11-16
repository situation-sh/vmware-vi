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


class VirtualDeviceConnectInfoMigrateConnectOpEnum(str, Enum):
    """
    Contains information about connectable virtual devices when the virtual machine restores from a migration.  Possible values: - `connect`: Attempt to connect the virtual device when the virtual machine   restores from a migration.      This property has no effect if it   is set on a device that is already connected. - `disconnect`: Attempt to disconnect the virtual device when the virtual machine   restores from a migration.      This property has no effect if it   is set on a device that is already disconnected. - `unset`: Unset the property, which resets the device to its default state.      Under most circumstances, a device will return to the same   connection state before the migration was initiated.  ***Since:*** vSphere API 6.7 
    """

    """
    allowed enum values
    """
    CONNECT = 'connect'
    DISCONNECT = 'disconnect'
    UNSET = 'unset'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualDeviceConnectInfoMigrateConnectOpEnum from a JSON string"""
        return cls(json.loads(json_str))


