# QueryHostPatchRequestType

The parameters of *HostPatchManager.QueryHostPatch_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostPatchManagerPatchManagerOperationSpec**](HostPatchManagerPatchManagerOperationSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_host_patch_request_type import QueryHostPatchRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryHostPatchRequestType from a JSON string
query_host_patch_request_type_instance = QueryHostPatchRequestType.from_json(json)
# print the JSON string representation of the object
print QueryHostPatchRequestType.to_json()

# convert the object into a dict
query_host_patch_request_type_dict = query_host_patch_request_type_instance.to_dict()
# create an instance of QueryHostPatchRequestType from a dict
query_host_patch_request_type_form_dict = query_host_patch_request_type.from_dict(query_host_patch_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


