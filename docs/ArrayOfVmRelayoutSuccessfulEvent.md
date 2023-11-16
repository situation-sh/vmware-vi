# ArrayOfVmRelayoutSuccessfulEvent

A boxed array of *VmRelayoutSuccessfulEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmRelayoutSuccessfulEvent]**](VmRelayoutSuccessfulEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_relayout_successful_event import ArrayOfVmRelayoutSuccessfulEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmRelayoutSuccessfulEvent from a JSON string
array_of_vm_relayout_successful_event_instance = ArrayOfVmRelayoutSuccessfulEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmRelayoutSuccessfulEvent.to_json()

# convert the object into a dict
array_of_vm_relayout_successful_event_dict = array_of_vm_relayout_successful_event_instance.to_dict()
# create an instance of ArrayOfVmRelayoutSuccessfulEvent from a dict
array_of_vm_relayout_successful_event_form_dict = array_of_vm_relayout_successful_event.from_dict(array_of_vm_relayout_successful_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


