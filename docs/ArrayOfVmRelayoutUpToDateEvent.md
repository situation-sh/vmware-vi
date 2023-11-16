# ArrayOfVmRelayoutUpToDateEvent

A boxed array of *VmRelayoutUpToDateEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmRelayoutUpToDateEvent]**](VmRelayoutUpToDateEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_relayout_up_to_date_event import ArrayOfVmRelayoutUpToDateEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmRelayoutUpToDateEvent from a JSON string
array_of_vm_relayout_up_to_date_event_instance = ArrayOfVmRelayoutUpToDateEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmRelayoutUpToDateEvent.to_json()

# convert the object into a dict
array_of_vm_relayout_up_to_date_event_dict = array_of_vm_relayout_up_to_date_event_instance.to_dict()
# create an instance of ArrayOfVmRelayoutUpToDateEvent from a dict
array_of_vm_relayout_up_to_date_event_form_dict = array_of_vm_relayout_up_to_date_event.from_dict(array_of_vm_relayout_up_to_date_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


