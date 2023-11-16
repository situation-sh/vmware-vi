# VirtualMachineFaultToleranceStateEnum

The FaultToleranceState type defines a simple set of states for a fault tolerant virtual machine: disabled, starting, and enabled.  Possible values: - `notConfigured`: This state indicates that the virtual machine has not been   configured for fault tolerance. - `disabled`: For a virtual machine that is the primary in a fault tolerant group,   this state indicates that the virtual machine has at least one   registered secondary, but no secondary is enabled.      For a virtual machine that is the secondary in a fault tolerant   group, this state indicates that the secondary is disabled. - `enabled`: For a virtual machine that is the primary in a fault tolerant group,   this state indicates that the virtual machine is not currently   powered on, but has at least one enabled secondary   For a virtual machine that is the secondary in a fault tolerant   group, this state indicates that the secondary is enabled, but is   not currently powered on. - `needSecondary`: For a virtual machine that is the primary in a fault tolerant group,   this state indicates that the virtual machine is powered on and   has at least one enabled secondary, but no secondary is currently   active.      This state is not valid for a virtual machine that is a secondary   in a fault tolerant group. - `starting`: For a virtual machine that is the primary in a fault tolerant group,   this state indicates that the virtual machine is powered on and has   at least one secondary that is synchronizing its state with the   primary.      For a virtual machine that is the secondary in a fault tolerant   group, this state indicates that the secondary is powered on and is   synchronizing its state with the primary virtual machine. - `running`: This state indicates that the virtual machine is running with fault   tolerance protection.    ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


