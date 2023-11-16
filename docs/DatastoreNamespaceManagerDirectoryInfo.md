# DatastoreNamespaceManagerDirectoryInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **int** | Size in MB of underlying object.  | 
**used** | **int** | Used size in MB in the VMFS volume.  | 

## Example

```python
from vmware_vi.models.datastore_namespace_manager_directory_info import DatastoreNamespaceManagerDirectoryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreNamespaceManagerDirectoryInfo from a JSON string
datastore_namespace_manager_directory_info_instance = DatastoreNamespaceManagerDirectoryInfo.from_json(json)
# print the JSON string representation of the object
print DatastoreNamespaceManagerDirectoryInfo.to_json()

# convert the object into a dict
datastore_namespace_manager_directory_info_dict = datastore_namespace_manager_directory_info_instance.to_dict()
# create an instance of DatastoreNamespaceManagerDirectoryInfo from a dict
datastore_namespace_manager_directory_info_form_dict = datastore_namespace_manager_directory_info.from_dict(datastore_namespace_manager_directory_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


