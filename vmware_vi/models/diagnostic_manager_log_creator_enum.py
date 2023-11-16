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


class DiagnosticManagerLogCreatorEnum(str, Enum):
    """
    Pre-defined constants for possible creators of log files.  Possible values: - `vpxd`: VirtualCenter service - `vpxa`: VirtualCenter agent - `hostd`: Host agent - `serverd`: Host server agent - `install`: Installation - `vpxClient`: Virtual infrastructure client - `recordLog`: System Record Log      ***Since:*** VI API 2.5 
    """

    """
    allowed enum values
    """
    VPXD = 'vpxd'
    VPXA = 'vpxa'
    HOSTD = 'hostd'
    SERVERD = 'serverd'
    INSTALL = 'install'
    VPXCLIENT = 'vpxClient'
    RECORDLOG = 'recordLog'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DiagnosticManagerLogCreatorEnum from a JSON string"""
        return cls(json.loads(json_str))


