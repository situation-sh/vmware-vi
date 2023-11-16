# VmPoweredOffEvent

This event records when a virtual machine finished powering off. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_powered_off_event import VmPoweredOffEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmPoweredOffEvent from a JSON string
vm_powered_off_event_instance = VmPoweredOffEvent.from_json(json)
# print the JSON string representation of the object
print VmPoweredOffEvent.to_json()

# convert the object into a dict
vm_powered_off_event_dict = vm_powered_off_event_instance.to_dict()
# create an instance of VmPoweredOffEvent from a dict
vm_powered_off_event_form_dict = vm_powered_off_event.from_dict(vm_powered_off_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


