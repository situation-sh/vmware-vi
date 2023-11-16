# ArrayOfHostDirectoryStoreInfo

A boxed array of *HostDirectoryStoreInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostDirectoryStoreInfo]**](HostDirectoryStoreInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_directory_store_info import ArrayOfHostDirectoryStoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostDirectoryStoreInfo from a JSON string
array_of_host_directory_store_info_instance = ArrayOfHostDirectoryStoreInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostDirectoryStoreInfo.to_json()

# convert the object into a dict
array_of_host_directory_store_info_dict = array_of_host_directory_store_info_instance.to_dict()
# create an instance of ArrayOfHostDirectoryStoreInfo from a dict
array_of_host_directory_store_info_form_dict = array_of_host_directory_store_info.from_dict(array_of_host_directory_store_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


