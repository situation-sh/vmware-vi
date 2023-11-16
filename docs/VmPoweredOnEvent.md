# VmPoweredOnEvent

This event records when a virtual machine finished powering on. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_powered_on_event import VmPoweredOnEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmPoweredOnEvent from a JSON string
vm_powered_on_event_instance = VmPoweredOnEvent.from_json(json)
# print the JSON string representation of the object
print VmPoweredOnEvent.to_json()

# convert the object into a dict
vm_powered_on_event_dict = vm_powered_on_event_instance.to_dict()
# create an instance of VmPoweredOnEvent from a dict
vm_powered_on_event_form_dict = vm_powered_on_event.from_dict(vm_powered_on_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


