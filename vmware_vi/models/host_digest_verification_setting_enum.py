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


class HostDigestVerificationSettingEnum(str, Enum):
    """
    This enum specifies the supported digest verification settings.  For NVMe over TCP connections, both header and data digests may be requested during the process of establishing the connection. For details, see: - NVM Express Technical Proposal 8000 - NVMe/TCP Transport,   Section 7.4.6, \"PDU Header and Data Digests\"    Possible values: - `digestDisabled`: Both header and data digest verification are disabled. - `headerOnly`: Only header digest verification is enabled. - `dataOnly`: Only data digest verification is enabled. - `headerAndData`: Both header and data digest verification are enabled.    ***Since:*** vSphere API 7.0.3.0 
    """

    """
    allowed enum values
    """
    DIGESTDISABLED = 'digestDisabled'
    HEADERONLY = 'headerOnly'
    DATAONLY = 'dataOnly'
    HEADERANDDATA = 'headerAndData'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostDigestVerificationSettingEnum from a JSON string"""
        return cls(json.loads(json_str))

