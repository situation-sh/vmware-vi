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


class ClusterPowerOnVmOptionEnum(str, Enum):
    """
    Defines the options for a Datacenter::powerOnVm() invocation.  Possible values: - `OverrideAutomationLevel`: Override the DRS automation level.      Value type: *DrsBehavior_enum*   Default value: current behavior - `ReserveResources`: Reserve resources for the powering-on VMs throughout the   power-on session.      When this option is set to true, the server   will return at most one recommended host per manual VM, and   the VM's reservations are held on the recommended host until   the VM is actually powered on (either by applying the   recommendation or by a power-on request on the VM), or until   the recommendation is cancelled, or until the recommendation   expires. The expiration time is currently set to 10   minutes. This option does not have an effect on automatic VMs   since their recommendations are executed immediately. This   option is effective on DRS clusters only.   Value type: boolean   Default value: false  ***Since:*** vSphere API 4.1 
    """

    """
    allowed enum values
    """
    OVERRIDEAUTOMATIONLEVEL = 'OverrideAutomationLevel'
    RESERVERESOURCES = 'ReserveResources'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ClusterPowerOnVmOptionEnum from a JSON string"""
        return cls(json.loads(json_str))


