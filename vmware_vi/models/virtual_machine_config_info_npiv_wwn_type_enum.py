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


class VirtualMachineConfigInfoNpivWwnTypeEnum(str, Enum):
    """
    The NPIV WWN source type.  Possible values: - `vc`: This set of WWNs is generated by VC server. - `host`: This set of WWNs is generated by Host Agent. - `external`: This set of WWNs is provided by the client.    ***Since:*** VI API 2.5 
    """

    """
    allowed enum values
    """
    VC = 'vc'
    HOST = 'host'
    EXTERNAL = 'external'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualMachineConfigInfoNpivWwnTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


