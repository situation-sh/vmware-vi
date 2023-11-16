# VmUnsupportedStartingEvent

This event records when an unsupported guest is powering on. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_id** | **str** |  | 

## Example

```python
from vmware_vi.models.vm_unsupported_starting_event import VmUnsupportedStartingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmUnsupportedStartingEvent from a JSON string
vm_unsupported_starting_event_instance = VmUnsupportedStartingEvent.from_json(json)
# print the JSON string representation of the object
print VmUnsupportedStartingEvent.to_json()

# convert the object into a dict
vm_unsupported_starting_event_dict = vm_unsupported_starting_event_instance.to_dict()
# create an instance of VmUnsupportedStartingEvent from a dict
vm_unsupported_starting_event_form_dict = vm_unsupported_starting_event.from_dict(vm_unsupported_starting_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


