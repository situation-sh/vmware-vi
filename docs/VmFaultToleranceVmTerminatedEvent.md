# VmFaultToleranceVmTerminatedEvent

This event records a secondary or primary VM is terminated.  The reason could be : divergence, lost connection to secondary, partial hardware failure of secondary, or by user.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason for the failure.  see *VirtualMachineNeedSecondaryReason_enum*  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.vm_fault_tolerance_vm_terminated_event import VmFaultToleranceVmTerminatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmFaultToleranceVmTerminatedEvent from a JSON string
vm_fault_tolerance_vm_terminated_event_instance = VmFaultToleranceVmTerminatedEvent.from_json(json)
# print the JSON string representation of the object
print VmFaultToleranceVmTerminatedEvent.to_json()

# convert the object into a dict
vm_fault_tolerance_vm_terminated_event_dict = vm_fault_tolerance_vm_terminated_event_instance.to_dict()
# create an instance of VmFaultToleranceVmTerminatedEvent from a dict
vm_fault_tolerance_vm_terminated_event_form_dict = vm_fault_tolerance_vm_terminated_event.from_dict(vm_fault_tolerance_vm_terminated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


