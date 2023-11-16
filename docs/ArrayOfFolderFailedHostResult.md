# ArrayOfFolderFailedHostResult

A boxed array of *FolderFailedHostResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FolderFailedHostResult]**](FolderFailedHostResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_folder_failed_host_result import ArrayOfFolderFailedHostResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFolderFailedHostResult from a JSON string
array_of_folder_failed_host_result_instance = ArrayOfFolderFailedHostResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfFolderFailedHostResult.to_json()

# convert the object into a dict
array_of_folder_failed_host_result_dict = array_of_folder_failed_host_result_instance.to_dict()
# create an instance of ArrayOfFolderFailedHostResult from a dict
array_of_folder_failed_host_result_form_dict = array_of_folder_failed_host_result.from_dict(array_of_folder_failed_host_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


