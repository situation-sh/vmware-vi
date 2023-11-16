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


class ClusterDasVmSettingsRestartPriorityEnum(str, Enum):
    """
    The *ClusterDasVmSettingsRestartPriority_enum* enum defines virtual machine restart priority values to resolve resource contention.  The priority determines the preference that HA gives to a virtual machine if sufficient capacity is not available to power on all failed virtual machines. For example, high priority virtual machines on a host get preference over low priority virtual machines.  All priority values are valid for the restart priority specified in a single virtual machine HA configuration (*ClusterDasVmConfigInfo.dasSettings*). All values except for <code>clusterRestartPriority</code> are valid for the cluster-wide default HA configuration for virtual machines (*ClusterDasConfigInfo.defaultVmSettings*).  Possible values: - `disabled`: vSphere HA is disabled for this virtual machine. - `lowest`: Virtual machines with this priority have the lowest chance of   powering on after a failure if there is insufficient capacity on   hosts to meet all virtual machine needs.      ***Since:*** vSphere API 6.5 - `low`: Virtual machines with this priority have a lower chance of powering   on after a failure if there is insufficient capacity on hosts to meet   all virtual machine needs. - `medium`: Virtual machines with this priority have an intermediate chance of   powering on after a failure if there is insufficient capacity on   hosts to meet all virtual machine needs. - `high`: Virtual machines with this priority have a higher chance of powering   on after a failure if there is insufficient capacity on hosts to meet   all virtual machine needs. - `highest`: Virtual machines with this priority have the highest chance of   powering on after a failure if there is insufficient capacity on   hosts to meet all virtual machine needs.      ***Since:*** vSphere API 6.5 - `clusterRestartPriority`: Virtual machines with this priority use the default restart   priority defined for the cluster that contains this virtual machine.    ***Since:*** VI API 2.5 
    """

    """
    allowed enum values
    """
    DISABLED = 'disabled'
    LOWEST = 'lowest'
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    HIGHEST = 'highest'
    CLUSTERRESTARTPRIORITY = 'clusterRestartPriority'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ClusterDasVmSettingsRestartPriorityEnum from a JSON string"""
        return cls(json.loads(json_str))


