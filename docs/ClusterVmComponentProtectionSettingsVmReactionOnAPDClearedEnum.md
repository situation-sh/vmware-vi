# ClusterVmComponentProtectionSettingsVmReactionOnAPDClearedEnum

If an APD condition clears after an APD timeout condition has been declared and before VM Component Protection service terminated the VM, the guestOS and application may no longer be operational.  VM Component Protection may be configured to reset the VM (*VirtualMachine.ResetVM_Task*) to restore the service of guest applications.  Possible values: - `none`: VM Component Protection service will not react after APD condition is cleared. - `reset`: VM Component Protection service will reset the VM after APD condition is cleared.      Note this only applies if the subject VM is still powered on. - `useClusterDefault`: VM will use the cluster default setting.      This option is only meaningful for   per-VM settings.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


