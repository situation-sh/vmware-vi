# VmCloneEvent

The is the base event for all clone operations. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_clone_event import VmCloneEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmCloneEvent from a JSON string
vm_clone_event_instance = VmCloneEvent.from_json(json)
# print the JSON string representation of the object
print VmCloneEvent.to_json()

# convert the object into a dict
vm_clone_event_dict = vm_clone_event_instance.to_dict()
# create an instance of VmCloneEvent from a dict
vm_clone_event_form_dict = vm_clone_event.from_dict(vm_clone_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


