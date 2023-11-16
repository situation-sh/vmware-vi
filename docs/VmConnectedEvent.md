# VmConnectedEvent

This event records that a virtual machine is connected. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_connected_event import VmConnectedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmConnectedEvent from a JSON string
vm_connected_event_instance = VmConnectedEvent.from_json(json)
# print the JSON string representation of the object
print VmConnectedEvent.to_json()

# convert the object into a dict
vm_connected_event_dict = vm_connected_event_instance.to_dict()
# create an instance of VmConnectedEvent from a dict
vm_connected_event_form_dict = vm_connected_event.from_dict(vm_connected_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


