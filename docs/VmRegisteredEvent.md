# VmRegisteredEvent

This event records that a virtual machine was successfully registered. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_registered_event import VmRegisteredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmRegisteredEvent from a JSON string
vm_registered_event_instance = VmRegisteredEvent.from_json(json)
# print the JSON string representation of the object
print VmRegisteredEvent.to_json()

# convert the object into a dict
vm_registered_event_dict = vm_registered_event_instance.to_dict()
# create an instance of VmRegisteredEvent from a dict
vm_registered_event_form_dict = vm_registered_event.from_dict(vm_registered_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


