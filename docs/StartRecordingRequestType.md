# StartRecordingRequestType

The parameters of *VirtualMachine.StartRecording_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name for the snapshot associated with this recording. The name need not be unique for this virtual machine.  | 
**description** | **str** | A description for the snapshot associated with this recording. If omitted, a default description may be provided.  | [optional] 

## Example

```python
from vmware_vi.models.start_recording_request_type import StartRecordingRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of StartRecordingRequestType from a JSON string
start_recording_request_type_instance = StartRecordingRequestType.from_json(json)
# print the JSON string representation of the object
print StartRecordingRequestType.to_json()

# convert the object into a dict
start_recording_request_type_dict = start_recording_request_type_instance.to_dict()
# create an instance of StartRecordingRequestType from a dict
start_recording_request_type_form_dict = start_recording_request_type.from_dict(start_recording_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


