# ArrayOfVmFaultToleranceVmTerminatedEvent

A boxed array of *VmFaultToleranceVmTerminatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmFaultToleranceVmTerminatedEvent]**](VmFaultToleranceVmTerminatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_fault_tolerance_vm_terminated_event import ArrayOfVmFaultToleranceVmTerminatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmFaultToleranceVmTerminatedEvent from a JSON string
array_of_vm_fault_tolerance_vm_terminated_event_instance = ArrayOfVmFaultToleranceVmTerminatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmFaultToleranceVmTerminatedEvent.to_json()

# convert the object into a dict
array_of_vm_fault_tolerance_vm_terminated_event_dict = array_of_vm_fault_tolerance_vm_terminated_event_instance.to_dict()
# create an instance of ArrayOfVmFaultToleranceVmTerminatedEvent from a dict
array_of_vm_fault_tolerance_vm_terminated_event_form_dict = array_of_vm_fault_tolerance_vm_terminated_event.from_dict(array_of_vm_fault_tolerance_vm_terminated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


