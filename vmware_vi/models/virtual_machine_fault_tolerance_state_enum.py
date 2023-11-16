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


class VirtualMachineFaultToleranceStateEnum(str, Enum):
    """
    The FaultToleranceState type defines a simple set of states for a fault tolerant virtual machine: disabled, starting, and enabled.  Possible values: - `notConfigured`: This state indicates that the virtual machine has not been   configured for fault tolerance. - `disabled`: For a virtual machine that is the primary in a fault tolerant group,   this state indicates that the virtual machine has at least one   registered secondary, but no secondary is enabled.      For a virtual machine that is the secondary in a fault tolerant   group, this state indicates that the secondary is disabled. - `enabled`: For a virtual machine that is the primary in a fault tolerant group,   this state indicates that the virtual machine is not currently   powered on, but has at least one enabled secondary   For a virtual machine that is the secondary in a fault tolerant   group, this state indicates that the secondary is enabled, but is   not currently powered on. - `needSecondary`: For a virtual machine that is the primary in a fault tolerant group,   this state indicates that the virtual machine is powered on and   has at least one enabled secondary, but no secondary is currently   active.      This state is not valid for a virtual machine that is a secondary   in a fault tolerant group. - `starting`: For a virtual machine that is the primary in a fault tolerant group,   this state indicates that the virtual machine is powered on and has   at least one secondary that is synchronizing its state with the   primary.      For a virtual machine that is the secondary in a fault tolerant   group, this state indicates that the secondary is powered on and is   synchronizing its state with the primary virtual machine. - `running`: This state indicates that the virtual machine is running with fault   tolerance protection.    ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    NOTCONFIGURED = 'notConfigured'
    DISABLED = 'disabled'
    ENABLED = 'enabled'
    NEEDSECONDARY = 'needSecondary'
    STARTING = 'starting'
    RUNNING = 'running'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VirtualMachineFaultToleranceStateEnum from a JSON string"""
        return cls(json.loads(json_str))


