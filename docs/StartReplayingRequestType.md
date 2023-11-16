# StartReplayingRequestType

The parameters of *VirtualMachine.StartReplaying_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replay_snapshot** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.start_replaying_request_type import StartReplayingRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of StartReplayingRequestType from a JSON string
start_replaying_request_type_instance = StartReplayingRequestType.from_json(json)
# print the JSON string representation of the object
print StartReplayingRequestType.to_json()

# convert the object into a dict
start_replaying_request_type_dict = start_replaying_request_type_instance.to_dict()
# create an instance of StartReplayingRequestType from a dict
start_replaying_request_type_form_dict = start_replaying_request_type.from_dict(start_replaying_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


