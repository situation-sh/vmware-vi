# ArrayOfVmStartReplayingEvent

A boxed array of *VmStartReplayingEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmStartReplayingEvent]**](VmStartReplayingEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_start_replaying_event import ArrayOfVmStartReplayingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmStartReplayingEvent from a JSON string
array_of_vm_start_replaying_event_instance = ArrayOfVmStartReplayingEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmStartReplayingEvent.to_json()

# convert the object into a dict
array_of_vm_start_replaying_event_dict = array_of_vm_start_replaying_event_instance.to_dict()
# create an instance of ArrayOfVmStartReplayingEvent from a dict
array_of_vm_start_replaying_event_form_dict = array_of_vm_start_replaying_event.from_dict(array_of_vm_start_replaying_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


