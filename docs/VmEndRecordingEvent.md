# VmEndRecordingEvent

Deprecated as of vSphere API 6.0.  This event indicates the end of a recording session on a virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_end_recording_event import VmEndRecordingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmEndRecordingEvent from a JSON string
vm_end_recording_event_instance = VmEndRecordingEvent.from_json(json)
# print the JSON string representation of the object
print VmEndRecordingEvent.to_json()

# convert the object into a dict
vm_end_recording_event_dict = vm_end_recording_event_instance.to_dict()
# create an instance of VmEndRecordingEvent from a dict
vm_end_recording_event_form_dict = vm_end_recording_event.from_dict(vm_end_recording_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


