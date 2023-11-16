# VmFaultToleranceTurnedOffEvent

This event records that all secondary virtual machines have been removed and fault tolerance protection turned off for this virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_fault_tolerance_turned_off_event import VmFaultToleranceTurnedOffEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmFaultToleranceTurnedOffEvent from a JSON string
vm_fault_tolerance_turned_off_event_instance = VmFaultToleranceTurnedOffEvent.from_json(json)
# print the JSON string representation of the object
print VmFaultToleranceTurnedOffEvent.to_json()

# convert the object into a dict
vm_fault_tolerance_turned_off_event_dict = vm_fault_tolerance_turned_off_event_instance.to_dict()
# create an instance of VmFaultToleranceTurnedOffEvent from a dict
vm_fault_tolerance_turned_off_event_form_dict = vm_fault_tolerance_turned_off_event.from_dict(vm_fault_tolerance_turned_off_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


