# VmCreatedEvent

This event records that a virtual machine was successfully created. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_created_event import VmCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmCreatedEvent from a JSON string
vm_created_event_instance = VmCreatedEvent.from_json(json)
# print the JSON string representation of the object
print VmCreatedEvent.to_json()

# convert the object into a dict
vm_created_event_dict = vm_created_event_instance.to_dict()
# create an instance of VmCreatedEvent from a dict
vm_created_event_form_dict = vm_created_event.from_dict(vm_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


