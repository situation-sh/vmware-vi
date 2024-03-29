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


class VAppIPAssignmentInfoProtocolsEnum(str, Enum):
    """
    IP protocols supported by the guest.  Possible values: - `IPv4`: The vApp supports IPv4 protocol. - `IPv6`: The vApp supports IPv6 protocol.    ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    IPV4 = 'IPv4'
    IPV6 = 'IPv6'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VAppIPAssignmentInfoProtocolsEnum from a JSON string"""
        return cls(json.loads(json_str))


