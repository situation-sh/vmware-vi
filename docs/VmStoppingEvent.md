# VmStoppingEvent

This event records a virtual machine stopping. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_stopping_event import VmStoppingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmStoppingEvent from a JSON string
vm_stopping_event_instance = VmStoppingEvent.from_json(json)
# print the JSON string representation of the object
print VmStoppingEvent.to_json()

# convert the object into a dict
vm_stopping_event_dict = vm_stopping_event_instance.to_dict()
# create an instance of VmStoppingEvent from a dict
vm_stopping_event_form_dict = vm_stopping_event.from_dict(vm_stopping_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


