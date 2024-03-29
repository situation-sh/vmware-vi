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


class HostProfileManagerTaskListRequirementEnum(str, Enum):
    """
    The *HostProfileManagerTaskListRequirement_enum* enum defines possible values for requirements when applying a *HostConfigSpec* object returned as part of a <code>generateConfigTaskList</code> operation.  Possible values: - `maintenanceModeRequired`: The ESXi host must be in maintenance mode before the task list can be   applied. - `rebootRequired`: The ESXi host must be rebooted after the task list is applied in order   for the new settings in the *HostConfigSpec* to take   effect on the host.    ***Since:*** vSphere API 6.0 
    """

    """
    allowed enum values
    """
    MAINTENANCEMODEREQUIRED = 'maintenanceModeRequired'
    REBOOTREQUIRED = 'rebootRequired'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of HostProfileManagerTaskListRequirementEnum from a JSON string"""
        return cls(json.loads(json_str))


