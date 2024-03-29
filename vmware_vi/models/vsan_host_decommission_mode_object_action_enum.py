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


class VsanHostDecommissionModeObjectActionEnum(str, Enum):
    """
    The action to take with regard to storage objects upon decommissioning a host from use with the VSAN service.  Possible values: - `noAction`: No special action should take place regarding VSAN data. - `ensureObjectAccessibility`: VSAN data reconfiguration should be performed to ensure storage   object accessibility. - `evacuateAllData`: VSAN data evacuation should be performed such that all storage   object data is removed from the host.    ***Since:*** vSphere API 5.5 
    """

    """
    allowed enum values
    """
    NOACTION = 'noAction'
    ENSUREOBJECTACCESSIBILITY = 'ensureObjectAccessibility'
    EVACUATEALLDATA = 'evacuateAllData'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VsanHostDecommissionModeObjectActionEnum from a JSON string"""
        return cls(json.loads(json_str))


