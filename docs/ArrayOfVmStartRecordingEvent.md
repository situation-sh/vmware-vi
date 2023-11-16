# ArrayOfVmStartRecordingEvent

A boxed array of *VmStartRecordingEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmStartRecordingEvent]**](VmStartRecordingEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_start_recording_event import ArrayOfVmStartRecordingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmStartRecordingEvent from a JSON string
array_of_vm_start_recording_event_instance = ArrayOfVmStartRecordingEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmStartRecordingEvent.to_json()

# convert the object into a dict
array_of_vm_start_recording_event_dict = array_of_vm_start_recording_event_instance.to_dict()
# create an instance of ArrayOfVmStartRecordingEvent from a dict
array_of_vm_start_recording_event_form_dict = array_of_vm_start_recording_event.from_dict(array_of_vm_start_recording_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


