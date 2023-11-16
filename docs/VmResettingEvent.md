# VmResettingEvent

This event records a virtual machine resetting. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_resetting_event import VmResettingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmResettingEvent from a JSON string
vm_resetting_event_instance = VmResettingEvent.from_json(json)
# print the JSON string representation of the object
print VmResettingEvent.to_json()

# convert the object into a dict
vm_resetting_event_dict = vm_resetting_event_instance.to_dict()
# create an instance of VmResettingEvent from a dict
vm_resetting_event_form_dict = vm_resetting_event.from_dict(vm_resetting_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


