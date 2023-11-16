# ReplicationVmFaultReasonForFaultEnum

Possible values: - `notConfigured`: *VirtualMachine* is not configured for replication - `poweredOff`: *VirtualMachine* is powered off (and is not undergoing   offline replication) - `suspended`: *VirtualMachine* is suspended (and is not undergoing   offline replication) - `poweredOn`: *VirtualMachine* is powered on - `offlineReplicating`: *VirtualMachine* is in the process of creating an   an offline instance. - `invalidState`: *VirtualMachine* is in an invalid state - `invalidInstanceId`: The specified instanceId does not match the *VirtualMachine*   instanceId - `closeDiskError`: *VirtualMachine* is in the process of creating an   offline instance and we are trying to disable it.      The first step is to close the offline disk. If closing disks   is not successful, throw this fault.      ***Since:*** vSphere API 6.5 - `groupExist`: *VirtualMachine* is trying to create a group already   owned by another VM.      ***Since:*** vSphere API 6.7  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


