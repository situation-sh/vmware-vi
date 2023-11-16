# SetMaxQueueDepthRequestType

The parameters of *HostDatastoreSystem.SetMaxQueueDepth*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**max_qdepth** | **int** | Max queue depth value for a datastore  | 

## Example

```python
from vmware_vi.models.set_max_queue_depth_request_type import SetMaxQueueDepthRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetMaxQueueDepthRequestType from a JSON string
set_max_queue_depth_request_type_instance = SetMaxQueueDepthRequestType.from_json(json)
# print the JSON string representation of the object
print SetMaxQueueDepthRequestType.to_json()

# convert the object into a dict
set_max_queue_depth_request_type_dict = set_max_queue_depth_request_type_instance.to_dict()
# create an instance of SetMaxQueueDepthRequestType from a dict
set_max_queue_depth_request_type_form_dict = set_max_queue_depth_request_type.from_dict(set_max_queue_depth_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


