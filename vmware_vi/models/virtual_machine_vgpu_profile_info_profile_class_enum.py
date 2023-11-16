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


class VirtualMachineVgpuProfileInfoProfileClassEnum(str, Enum):
    """
    Possible values for profile class.  Possible values: - `compute` - `quadro`  ***Since:*** vSphere API 7.0.3.0 
    """

    """
    allowed enum values
    """
    COMPUTE = 'compute'
    QUADRO = 'quadro'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualMachineVgpuProfileInfoProfileClassEnum from a JSON string"""
        return cls(json.loads(json_str))


