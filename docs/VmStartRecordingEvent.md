# VmStartRecordingEvent

Deprecated as of vSphere API 6.0.  This event indicates the start of a recording session on a virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_start_recording_event import VmStartRecordingEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmStartRecordingEvent from a JSON string
vm_start_recording_event_instance = VmStartRecordingEvent.from_json(json)
# print the JSON string representation of the object
print VmStartRecordingEvent.to_json()

# convert the object into a dict
vm_start_recording_event_dict = vm_start_recording_event_instance.to_dict()
# create an instance of VmStartRecordingEvent from a dict
vm_start_recording_event_form_dict = vm_start_recording_event.from_dict(vm_start_recording_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


