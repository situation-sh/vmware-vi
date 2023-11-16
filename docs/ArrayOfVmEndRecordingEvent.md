# ArrayOfVmEndRecordingEvent

A boxed array of *VmEndRecordingEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmEndRecordingEvent]**](VmEndRecordingEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_end_recording_event import ArrayOfVmEndRecordingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmEndRecordingEvent from a JSON string
array_of_vm_end_recording_event_instance = ArrayOfVmEndRecordingEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmEndRecordingEvent.to_json()

# convert the object into a dict
array_of_vm_end_recording_event_dict = array_of_vm_end_recording_event_instance.to_dict()
# create an instance of ArrayOfVmEndRecordingEvent from a dict
array_of_vm_end_recording_event_form_dict = array_of_vm_end_recording_event.from_dict(array_of_vm_end_recording_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


