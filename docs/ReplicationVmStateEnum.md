# ReplicationVmStateEnum

Describes the current state of a replicated *VirtualMachine*  Possible values: - `none`: The *VirtualMachine* has no current replication state.      This is a virtual machine that is configured for replication, but is   powered off and not undergoing offline replication. - `paused`: The *VirtualMachine* replication is paused. - `syncing`: One or more of the *VirtualMachine* disks is in the   process of an initial synchronization with the remote site. - `idle`: The *VirtualMachine* is being replicated but is not   currently in the process of having a consistent instance created. - `active`: The *VirtualMachine* is in the process of having   a consistent instance created. - `error`: The *VirtualMachine* is unable to replicate due to   errors.      XXX Currently unused.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


