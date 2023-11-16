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


class VirtualVmxnet3VrdmaOptionDeviceProtocolsEnum(str, Enum):
    """
    The enumeration of all known valid VRDMA device protocols.  Possible values: - `rocev1`: A RoCEv1 device. - `rocev2`: A RoCEv2 device.    ***Since:*** vSphere API 6.7 
    """

    """
    allowed enum values
    """
    ROCEV1 = 'rocev1'
    ROCEV2 = 'rocev2'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualVmxnet3VrdmaOptionDeviceProtocolsEnum from a JSON string"""
        return cls(json.loads(json_str))


