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


class DistributedVirtualPortgroupPortgroupTypeEnum(str, Enum):
    """
    The *DistributedVirtualPortgroupPortgroupType_enum* enum defines the distributed virtual portgroup types (*DistributedVirtualPortgroup*.*DistributedVirtualPortgroup.config*.*DVPortgroupConfigInfo.type*).  Early binding specifies a static set of ports that are created when you create the distributed virtual portgroup. An ephemeral portgroup uses dynamic ports that are created when you power on a virtual machine.  Possible values: - `earlyBinding`: A free *DistributedVirtualPort* will be selected and assigned to   a *VirtualMachine* when the virtual machine is reconfigured to   connect to the portgroup. - `lateBinding`:       Deprecated as of vSphere API 5.0.      A free *DistributedVirtualPort* will be selected and   assigned to a *VirtualMachine* when the virtual machine is   powered on. - `ephemeral`: A *DistributedVirtualPort* will be created and assigned to a   *VirtualMachine* when the virtual machine is powered on, and will   be deleted when the virtual machine is powered off.      An ephemeral portgroup has   no limit on the number of ports that can be a part of this portgroup.   In cases where the vCenter Server is unavailable the host can   create conflict ports in this portgroup to be used by a virtual machine   at power on.  ***Since:*** vSphere API 4.0 
    """

    """
    allowed enum values
    """
    EARLYBINDING = 'earlyBinding'
    LATEBINDING = 'lateBinding'
    EPHEMERAL = 'ephemeral'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DistributedVirtualPortgroupPortgroupTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


