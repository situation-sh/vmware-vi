# VmRelayoutSuccessfulEvent

This event records that a virtual machine was successfully converted to the new virtual machine format on a VMFS3 volume. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_relayout_successful_event import VmRelayoutSuccessfulEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmRelayoutSuccessfulEvent from a JSON string
vm_relayout_successful_event_instance = VmRelayoutSuccessfulEvent.from_json(json)
# print the JSON string representation of the object
print VmRelayoutSuccessfulEvent.to_json()

# convert the object into a dict
vm_relayout_successful_event_dict = vm_relayout_successful_event_instance.to_dict()
# create an instance of VmRelayoutSuccessfulEvent from a dict
vm_relayout_successful_event_form_dict = vm_relayout_successful_event.from_dict(vm_relayout_successful_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


