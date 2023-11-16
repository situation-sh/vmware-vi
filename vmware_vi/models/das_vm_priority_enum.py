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


class DasVmPriorityEnum(str, Enum):
    """
    Deprecated as of VI API 2.5, use *ClusterDasVmSettingsRestartPriority_enum*.  The priority of the virtual machine determines the preference given to it if sufficient capacity is not available to power on all failed virtual machines.  For example, high priority virtual machines on a host get preference over low priority virtual machines.  Possible values: - `disabled`: vSphere HA is disabled for this virtual machine. - `low`: Virtual machines with this priority have a lower chance of powering on after a   failure if there is insufficient capacity on hosts to meet all virtual machine   needs. - `medium`: Virtual machines with this priority have an intermediate chance of powering   on after a failure if there is insufficient capacity on hosts to meet all   virtual machine needs. - `high`: Virtual machines with this priority have a higher chance of powering on after a   failure if there is insufficient capacity on hosts to meet all virtual machine   needs. 
    """

    """
    allowed enum values
    """
    DISABLED = 'disabled'
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DasVmPriorityEnum from a JSON string"""
        return cls(json.loads(json_str))


