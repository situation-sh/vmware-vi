# VmRelayoutUpToDateEvent

This event records that a virtual machine is already in the correct format.  No relay out is necessary. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_relayout_up_to_date_event import VmRelayoutUpToDateEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmRelayoutUpToDateEvent from a JSON string
vm_relayout_up_to_date_event_instance = VmRelayoutUpToDateEvent.from_json(json)
# print the JSON string representation of the object
print VmRelayoutUpToDateEvent.to_json()

# convert the object into a dict
vm_relayout_up_to_date_event_dict = vm_relayout_up_to_date_event_instance.to_dict()
# create an instance of VmRelayoutUpToDateEvent from a dict
vm_relayout_up_to_date_event_form_dict = vm_relayout_up_to_date_event.from_dict(vm_relayout_up_to_date_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


