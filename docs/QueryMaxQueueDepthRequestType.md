# QueryMaxQueueDepthRequestType

The parameters of *HostDatastoreSystem.QueryMaxQueueDepth*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.query_max_queue_depth_request_type import QueryMaxQueueDepthRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMaxQueueDepthRequestType from a JSON string
query_max_queue_depth_request_type_instance = QueryMaxQueueDepthRequestType.from_json(json)
# print the JSON string representation of the object
print QueryMaxQueueDepthRequestType.to_json()

# convert the object into a dict
query_max_queue_depth_request_type_dict = query_max_queue_depth_request_type_instance.to_dict()
# create an instance of QueryMaxQueueDepthRequestType from a dict
query_max_queue_depth_request_type_form_dict = query_max_queue_depth_request_type.from_dict(query_max_queue_depth_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


