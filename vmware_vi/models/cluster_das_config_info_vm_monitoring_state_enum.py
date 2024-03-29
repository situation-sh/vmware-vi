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


class ClusterDasConfigInfoVmMonitoringStateEnum(str, Enum):
    """
    The *ClusterDasConfigInfoVmMonitoringState_enum* enum defines values that indicate the state of Virtual Machine Health Monitoring.  Health Monitoring uses the vmTools (guest) and application agent heartbeat modules. You can configure HA to respond to heartbeat failures of either one or both modules. You can also disable the HA response to heartbeat failures. - To set the cluster default for health monitoring, use the   ClusterConfigSpecEx.dasConfig.*ClusterDasConfigInfo.vmMonitoring* property. - To set health monitoring for a virtual machine, use the   ClusterConfigSpecEx.dasVmConfigSpec.info.dasSettings.*ClusterDasVmSettings.vmToolsMonitoringSettings* property. - To retrieve the current state of health monitoring (cluster setting), use the   ClusterConfigInfoEx.dasConfig.*ClusterDasConfigInfo.vmMonitoring*   property. - To retrieve the current state of health monitoring for a virtual machine, use the   ClusterConfigInfoEx.dasVmConfig\\[\\].dasSettings.vmToolsMonitoringSettings.*ClusterVmToolsMonitoringSettings.vmMonitoring*   property.    Possible values: - `vmMonitoringDisabled`: Virtual machine health monitoring is disabled.      In this state,   HA response to guest and application heartbeat failures are disabled. - `vmMonitoringOnly`: HA response to guest heartbeat failure is enabled.      To retrieve the guest heartbeat status, use the   *VirtualMachine*.*VirtualMachine.guestHeartbeatStatus*   property. - `vmAndAppMonitoring`: HA response to both guest and application heartbeat failure is enabled.   - To retrieve the guest heartbeat status, use the     *VirtualMachine*.*VirtualMachine.guestHeartbeatStatus*     property.   - To retrieve the application heartbeat status, use the     *GuestInfo*.*GuestInfo.appHeartbeatStatus*     property.      ***Since:*** vSphere API 4.1 
    """

    """
    allowed enum values
    """
    VMMONITORINGDISABLED = 'vmMonitoringDisabled'
    VMMONITORINGONLY = 'vmMonitoringOnly'
    VMANDAPPMONITORING = 'vmAndAppMonitoring'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ClusterDasConfigInfoVmMonitoringStateEnum from a JSON string"""
        return cls(json.loads(json_str))


