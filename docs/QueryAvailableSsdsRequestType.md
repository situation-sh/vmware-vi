# QueryAvailableSsdsRequestType

The parameters of *HostStorageSystem.QueryAvailableSsds*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vffs_path** | **str** | The path of the VFFS to extend. See *FileSystemMountInfo*.  | [optional] 

## Example

```python
from vmware_vi.models.query_available_ssds_request_type import QueryAvailableSsdsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryAvailableSsdsRequestType from a JSON string
query_available_ssds_request_type_instance = QueryAvailableSsdsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryAvailableSsdsRequestType.to_json()

# convert the object into a dict
query_available_ssds_request_type_dict = query_available_ssds_request_type_instance.to_dict()
# create an instance of QueryAvailableSsdsRequestType from a dict
query_available_ssds_request_type_form_dict = query_available_ssds_request_type.from_dict(query_available_ssds_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


