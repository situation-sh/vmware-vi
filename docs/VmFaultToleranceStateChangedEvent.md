# VmFaultToleranceStateChangedEvent

This event records a fault tolerance state change.  A default alarm will be triggered upon this event, which would change the vm state: the vm state is red if the newState is needSecondary; the vm state is yellow if the newState is disabled; the vm state is green if the newState is notConfigured, starting, enabled or running  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_state** | [**VirtualMachineFaultToleranceStateEnum**](VirtualMachineFaultToleranceStateEnum.md) |  | 
**new_state** | [**VirtualMachineFaultToleranceStateEnum**](VirtualMachineFaultToleranceStateEnum.md) |  | 

## Example

```python
from vmware_vi.models.vm_fault_tolerance_state_changed_event import VmFaultToleranceStateChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmFaultToleranceStateChangedEvent from a JSON string
vm_fault_tolerance_state_changed_event_instance = VmFaultToleranceStateChangedEvent.from_json(json)
# print the JSON string representation of the object
print VmFaultToleranceStateChangedEvent.to_json()

# convert the object into a dict
vm_fault_tolerance_state_changed_event_dict = vm_fault_tolerance_state_changed_event_instance.to_dict()
# create an instance of VmFaultToleranceStateChangedEvent from a dict
vm_fault_tolerance_state_changed_event_form_dict = vm_fault_tolerance_state_changed_event.from_dict(vm_fault_tolerance_state_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


