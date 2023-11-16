# ArrayOfFolderBatchAddStandaloneHostsResult

A boxed array of *FolderBatchAddStandaloneHostsResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FolderBatchAddStandaloneHostsResult]**](FolderBatchAddStandaloneHostsResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_folder_batch_add_standalone_hosts_result import ArrayOfFolderBatchAddStandaloneHostsResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFolderBatchAddStandaloneHostsResult from a JSON string
array_of_folder_batch_add_standalone_hosts_result_instance = ArrayOfFolderBatchAddStandaloneHostsResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfFolderBatchAddStandaloneHostsResult.to_json()

# convert the object into a dict
array_of_folder_batch_add_standalone_hosts_result_dict = array_of_folder_batch_add_standalone_hosts_result_instance.to_dict()
# create an instance of ArrayOfFolderBatchAddStandaloneHostsResult from a dict
array_of_folder_batch_add_standalone_hosts_result_form_dict = array_of_folder_batch_add_standalone_hosts_result.from_dict(array_of_folder_batch_add_standalone_hosts_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


