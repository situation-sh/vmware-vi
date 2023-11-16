# VmFailedToPowerOffEvent

This event records a failure to power off a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.vm_failed_to_power_off_event import VmFailedToPowerOffEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmFailedToPowerOffEvent from a JSON string
vm_failed_to_power_off_event_instance = VmFailedToPowerOffEvent.from_json(json)
# print the JSON string representation of the object
print VmFailedToPowerOffEvent.to_json()

# convert the object into a dict
vm_failed_to_power_off_event_dict = vm_failed_to_power_off_event_instance.to_dict()
# create an instance of VmFailedToPowerOffEvent from a dict
vm_failed_to_power_off_event_form_dict = vm_failed_to_power_off_event.from_dict(vm_failed_to_power_off_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


