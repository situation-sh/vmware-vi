# VmResumingEvent

This event records a virtual machine resuming. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_resuming_event import VmResumingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmResumingEvent from a JSON string
vm_resuming_event_instance = VmResumingEvent.from_json(json)
# print the JSON string representation of the object
print VmResumingEvent.to_json()

# convert the object into a dict
vm_resuming_event_dict = vm_resuming_event_instance.to_dict()
# create an instance of VmResumingEvent from a dict
vm_resuming_event_form_dict = vm_resuming_event.from_dict(vm_resuming_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


