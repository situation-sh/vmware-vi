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


class QuiesceModeEnum(str, Enum):
    """
    Quiescing is a boolean flag in *ReplicationConfigSpec* and QuiesceModeType describes the supported quiesce mode for *VirtualMachine*.  If application quiescing fails, HBR would attempt filesystem quiescing and if even filesystem quiescing fails, then we would just create a crash consistent instance.  Possible values: - `application`: HBR supports application quescing for this   *VirtualMachine*. - `filesystem`: HBR supports filesystem quescing for this   *VirtualMachine*. - `none`: HBR does not support quescing for this   *VirtualMachine*.    ***Since:*** vSphere API 6.0 
    """

    """
    allowed enum values
    """
    APPLICATION = 'application'
    FILESYSTEM = 'filesystem'
    NONE = 'none'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of QuiesceModeEnum from a JSON string"""
        return cls(json.loads(json_str))


