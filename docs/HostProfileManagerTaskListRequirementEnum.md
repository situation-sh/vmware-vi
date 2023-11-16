# HostProfileManagerTaskListRequirementEnum

The *HostProfileManagerTaskListRequirement_enum* enum defines possible values for requirements when applying a *HostConfigSpec* object returned as part of a <code>generateConfigTaskList</code> operation.  Possible values: - `maintenanceModeRequired`: The ESXi host must be in maintenance mode before the task list can be   applied. - `rebootRequired`: The ESXi host must be rebooted after the task list is applied in order   for the new settings in the *HostConfigSpec* to take   effect on the host.    ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


