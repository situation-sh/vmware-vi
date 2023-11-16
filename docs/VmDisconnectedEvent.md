# VmDisconnectedEvent

This event records that a virtual machine disconnected. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_disconnected_event import VmDisconnectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmDisconnectedEvent from a JSON string
vm_disconnected_event_instance = VmDisconnectedEvent.from_json(json)
# print the JSON string representation of the object
print VmDisconnectedEvent.to_json()

# convert the object into a dict
vm_disconnected_event_dict = vm_disconnected_event_instance.to_dict()
# create an instance of VmDisconnectedEvent from a dict
vm_disconnected_event_form_dict = vm_disconnected_event.from_dict(vm_disconnected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


