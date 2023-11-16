# ArrayOfVmFailedRelayoutEvent

A boxed array of *VmFailedRelayoutEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmFailedRelayoutEvent]**](VmFailedRelayoutEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_failed_relayout_event import ArrayOfVmFailedRelayoutEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmFailedRelayoutEvent from a JSON string
array_of_vm_failed_relayout_event_instance = ArrayOfVmFailedRelayoutEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmFailedRelayoutEvent.to_json()

# convert the object into a dict
array_of_vm_failed_relayout_event_dict = array_of_vm_failed_relayout_event_instance.to_dict()
# create an instance of ArrayOfVmFailedRelayoutEvent from a dict
array_of_vm_failed_relayout_event_form_dict = array_of_vm_failed_relayout_event.from_dict(array_of_vm_failed_relayout_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


