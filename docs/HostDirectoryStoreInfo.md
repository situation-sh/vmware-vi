# HostDirectoryStoreInfo

*HostDirectoryStoreInfo* is a base class for objects that provide information about directory-based authentication stores.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_directory_store_info import HostDirectoryStoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostDirectoryStoreInfo from a JSON string
host_directory_store_info_instance = HostDirectoryStoreInfo.from_json(json)
# print the JSON string representation of the object
print HostDirectoryStoreInfo.to_json()

# convert the object into a dict
host_directory_store_info_dict = host_directory_store_info_instance.to_dict()
# create an instance of HostDirectoryStoreInfo from a dict
host_directory_store_info_form_dict = host_directory_store_info.from_dict(host_directory_store_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


