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


class VsanHostNodeStateEnum(str, Enum):
    """
    A *VsanHostNodeState_enum* represents the state of participation of a host in the VSAN service.  See also *VsanHostClusterStatus*, *VsanHostClusterStatusState*.  Possible values: - `error`: The node is enabled for the VSAN service but has some configuration   error which prevents participation. - `disabled`: The node is disabled for the VSAN service. - `agent`: The node is enabled for the VSAN service and is serving as an agent. - `master`: The node is enabled for the VSAN service and is serving as the master. - `backup`: The node is enabled for the VSAN service and is serving as the backup. - `starting`: The node is starting the VSAN service; this state is considered   transitory. - `stopping`: The node is stopping the VSAN service; this state is considered   transitory. - `enteringMaintenanceMode`: The node is entering maintenance mode; this state is considered   transitory.      See also *HostSystem.EnterMaintenanceMode_Task*. - `exitingMaintenanceMode`: The node is exiting maintenance mode; this state is considered   transitory.      See also *HostSystem.ExitMaintenanceMode_Task*. - `decommissioning`: The node is being decommissioned from the VSAN service; this state is   considered transitory.    ***Since:*** vSphere API 5.5 
    """

    """
    allowed enum values
    """
    ERROR = 'error'
    DISABLED = 'disabled'
    AGENT = 'agent'
    MASTER = 'master'
    BACKUP = 'backup'
    STARTING = 'starting'
    STOPPING = 'stopping'
    ENTERINGMAINTENANCEMODE = 'enteringMaintenanceMode'
    EXITINGMAINTENANCEMODE = 'exitingMaintenanceMode'
    DECOMMISSIONING = 'decommissioning'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of VsanHostNodeStateEnum from a JSON string"""
        return cls(json.loads(json_str))


