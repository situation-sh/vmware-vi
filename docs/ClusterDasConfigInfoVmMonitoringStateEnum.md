# ClusterDasConfigInfoVmMonitoringStateEnum

The *ClusterDasConfigInfoVmMonitoringState_enum* enum defines values that indicate the state of Virtual Machine Health Monitoring.  Health Monitoring uses the vmTools (guest) and application agent heartbeat modules. You can configure HA to respond to heartbeat failures of either one or both modules. You can also disable the HA response to heartbeat failures. - To set the cluster default for health monitoring, use the   ClusterConfigSpecEx.dasConfig.*ClusterDasConfigInfo.vmMonitoring* property. - To set health monitoring for a virtual machine, use the   ClusterConfigSpecEx.dasVmConfigSpec.info.dasSettings.*ClusterDasVmSettings.vmToolsMonitoringSettings* property. - To retrieve the current state of health monitoring (cluster setting), use the   ClusterConfigInfoEx.dasConfig.*ClusterDasConfigInfo.vmMonitoring*   property. - To retrieve the current state of health monitoring for a virtual machine, use the   ClusterConfigInfoEx.dasVmConfig\\[\\].dasSettings.vmToolsMonitoringSettings.*ClusterVmToolsMonitoringSettings.vmMonitoring*   property.    Possible values: - `vmMonitoringDisabled`: Virtual machine health monitoring is disabled.      In this state,   HA response to guest and application heartbeat failures are disabled. - `vmMonitoringOnly`: HA response to guest heartbeat failure is enabled.      To retrieve the guest heartbeat status, use the   *VirtualMachine*.*VirtualMachine.guestHeartbeatStatus*   property. - `vmAndAppMonitoring`: HA response to both guest and application heartbeat failure is enabled.   - To retrieve the guest heartbeat status, use the     *VirtualMachine*.*VirtualMachine.guestHeartbeatStatus*     property.   - To retrieve the application heartbeat status, use the     *GuestInfo*.*GuestInfo.appHeartbeatStatus*     property.      ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


