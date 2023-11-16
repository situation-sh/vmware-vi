# VirtualMachinePowerStateEnum

The PowerState type defines a simple set of states for a virtual machine: poweredOn, poweredOff, and suspended.  This type does not model substates, such as when a task is running to change the virtual machine state. If the virtual machine is in a state with a task in progress, it transitions to a new state when the task completes. For example, a virtual machine continues to be in the poweredOn state while a suspend task is running, and changes to the suspended state once the task finishes.  As a consequence of this approach, clients interested in monitoring the status of a virtual machine should typically track the *activeTask* data object in addition to the *powerState* object.  Possible values: - `poweredOff`: The virtual machine is currently powered off. - `poweredOn`: The virtual machine is currently powered on. - `suspended`: The virtual machine is currently suspended. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


