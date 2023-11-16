# VsanHostNodeStateEnum

A *VsanHostNodeState_enum* represents the state of participation of a host in the VSAN service.  See also *VsanHostClusterStatus*, *VsanHostClusterStatusState*.  Possible values: - `error`: The node is enabled for the VSAN service but has some configuration   error which prevents participation. - `disabled`: The node is disabled for the VSAN service. - `agent`: The node is enabled for the VSAN service and is serving as an agent. - `master`: The node is enabled for the VSAN service and is serving as the master. - `backup`: The node is enabled for the VSAN service and is serving as the backup. - `starting`: The node is starting the VSAN service; this state is considered   transitory. - `stopping`: The node is stopping the VSAN service; this state is considered   transitory. - `enteringMaintenanceMode`: The node is entering maintenance mode; this state is considered   transitory.      See also *HostSystem.EnterMaintenanceMode_Task*. - `exitingMaintenanceMode`: The node is exiting maintenance mode; this state is considered   transitory.      See also *HostSystem.ExitMaintenanceMode_Task*. - `decommissioning`: The node is being decommissioned from the VSAN service; this state is   considered transitory.    ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


