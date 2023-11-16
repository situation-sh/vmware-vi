# QueryVsanObjectUuidsByFilterRequestType

The parameters of *HostVsanInternalSystem.QueryVsanObjectUuidsByFilter*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[str]** | Objects UUID will be checked against the filtering conditions.  | [optional] 
**limit** | **int** | To limit the size of the result set.  | [optional] 
**version** | **int** | Filtering condition 1: object version.  | [optional] 

## Example

```python
from vmware_vi.models.query_vsan_object_uuids_by_filter_request_type import QueryVsanObjectUuidsByFilterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryVsanObjectUuidsByFilterRequestType from a JSON string
query_vsan_object_uuids_by_filter_request_type_instance = QueryVsanObjectUuidsByFilterRequestType.from_json(json)
# print the JSON string representation of the object
print QueryVsanObjectUuidsByFilterRequestType.to_json()

# convert the object into a dict
query_vsan_object_uuids_by_filter_request_type_dict = query_vsan_object_uuids_by_filter_request_type_instance.to_dict()
# create an instance of QueryVsanObjectUuidsByFilterRequestType from a dict
query_vsan_object_uuids_by_filter_request_type_form_dict = query_vsan_object_uuids_by_filter_request_type.from_dict(query_vsan_object_uuids_by_filter_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


