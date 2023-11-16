# QuerySyncingVsanObjectsRequestType

The parameters of *HostVsanInternalSystem.QuerySyncingVsanObjects*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[str]** | List of VSAN/DOM object UUIDs to restrict search to.  | [optional] 

## Example

```python
from vmware_vi.models.query_syncing_vsan_objects_request_type import QuerySyncingVsanObjectsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QuerySyncingVsanObjectsRequestType from a JSON string
query_syncing_vsan_objects_request_type_instance = QuerySyncingVsanObjectsRequestType.from_json(json)
# print the JSON string representation of the object
print QuerySyncingVsanObjectsRequestType.to_json()

# convert the object into a dict
query_syncing_vsan_objects_request_type_dict = query_syncing_vsan_objects_request_type_instance.to_dict()
# create an instance of QuerySyncingVsanObjectsRequestType from a dict
query_syncing_vsan_objects_request_type_form_dict = query_syncing_vsan_objects_request_type.from_dict(query_syncing_vsan_objects_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


