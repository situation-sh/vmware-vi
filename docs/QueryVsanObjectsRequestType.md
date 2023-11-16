# QueryVsanObjectsRequestType

The parameters of *HostVsanInternalSystem.QueryVsanObjects*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[str]** | List of VSAN/DOM object UUIDs.  | [optional] 

## Example

```python
from vmware_vi.models.query_vsan_objects_request_type import QueryVsanObjectsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryVsanObjectsRequestType from a JSON string
query_vsan_objects_request_type_instance = QueryVsanObjectsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryVsanObjectsRequestType.to_json()

# convert the object into a dict
query_vsan_objects_request_type_dict = query_vsan_objects_request_type_instance.to_dict()
# create an instance of QueryVsanObjectsRequestType from a dict
query_vsan_objects_request_type_form_dict = query_vsan_objects_request_type.from_dict(query_vsan_objects_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


