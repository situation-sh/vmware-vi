# VmEmigratingEvent

This event records a virtual machine emigration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_emigrating_event import VmEmigratingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmEmigratingEvent from a JSON string
vm_emigrating_event_instance = VmEmigratingEvent.from_json(json)
# print the JSON string representation of the object
print VmEmigratingEvent.to_json()

# convert the object into a dict
vm_emigrating_event_dict = vm_emigrating_event_instance.to_dict()
# create an instance of VmEmigratingEvent from a dict
vm_emigrating_event_form_dict = vm_emigrating_event.from_dict(vm_emigrating_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


