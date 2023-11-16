# VmStartingEvent

This event records a virtual machine powering on. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_starting_event import VmStartingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmStartingEvent from a JSON string
vm_starting_event_instance = VmStartingEvent.from_json(json)
# print the JSON string representation of the object
print VmStartingEvent.to_json()

# convert the object into a dict
vm_starting_event_dict = vm_starting_event_instance.to_dict()
# create an instance of VmStartingEvent from a dict
vm_starting_event_form_dict = vm_starting_event.from_dict(vm_starting_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


