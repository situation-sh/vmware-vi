# IncreaseDirectorySizeRequestType

The parameters of *DatastoreNamespaceManager.IncreaseDirectorySize*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**stable_name** | **str** | stable vmfs path of the top-level directory  | 
**size** | **int** | the desired final size in MB of the directory, not a diff from the current size; should be more than current size  | 

## Example

```python
from vmware_vi.models.increase_directory_size_request_type import IncreaseDirectorySizeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of IncreaseDirectorySizeRequestType from a JSON string
increase_directory_size_request_type_instance = IncreaseDirectorySizeRequestType.from_json(json)
# print the JSON string representation of the object
print IncreaseDirectorySizeRequestType.to_json()

# convert the object into a dict
increase_directory_size_request_type_dict = increase_directory_size_request_type_instance.to_dict()
# create an instance of IncreaseDirectorySizeRequestType from a dict
increase_directory_size_request_type_form_dict = increase_directory_size_request_type.from_dict(increase_directory_size_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


