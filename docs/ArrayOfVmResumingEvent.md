# ArrayOfVmResumingEvent

A boxed array of *VmResumingEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmResumingEvent]**](VmResumingEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_resuming_event import ArrayOfVmResumingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmResumingEvent from a JSON string
array_of_vm_resuming_event_instance = ArrayOfVmResumingEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmResumingEvent.to_json()

# convert the object into a dict
array_of_vm_resuming_event_dict = array_of_vm_resuming_event_instance.to_dict()
# create an instance of ArrayOfVmResumingEvent from a dict
array_of_vm_resuming_event_form_dict = array_of_vm_resuming_event.from_dict(array_of_vm_resuming_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


