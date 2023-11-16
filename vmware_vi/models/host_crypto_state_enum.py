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


class HostCryptoStateEnum(str, Enum):
    """
    Defines a host's encryption state  Possible values: - `incapable`: The host is not safe for receiving sensitive material. - `prepared`: The host is prepared for receiving sensitive material   but does not have a host key set yet. - `safe`: The host is crypto safe and has a host key set. - `pendingIncapable`: The host is explicitly crypto disabled and pending reboot to be   applied.      When host is in this state, creating encrypted virtual   machines is not allowed, but still need a reboot to totally clean   up and enter incapable state.      ***Since:*** vSphere API 7.0  ***Since:*** vSphere API 6.5 
    """

    """
    allowed enum values
    """
    INCAPABLE = 'incapable'
    PREPARED = 'prepared'
    SAFE = 'safe'
    PENDINGINCAPABLE = 'pendingIncapable'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostCryptoStateEnum from a JSON string"""
        return cls(json.loads(json_str))


