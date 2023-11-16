# ArrayOfFolderBatchAddHostsToClusterResult

A boxed array of *FolderBatchAddHostsToClusterResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FolderBatchAddHostsToClusterResult]**](FolderBatchAddHostsToClusterResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_folder_batch_add_hosts_to_cluster_result import ArrayOfFolderBatchAddHostsToClusterResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFolderBatchAddHostsToClusterResult from a JSON string
array_of_folder_batch_add_hosts_to_cluster_result_instance = ArrayOfFolderBatchAddHostsToClusterResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfFolderBatchAddHostsToClusterResult.to_json()

# convert the object into a dict
array_of_folder_batch_add_hosts_to_cluster_result_dict = array_of_folder_batch_add_hosts_to_cluster_result_instance.to_dict()
# create an instance of ArrayOfFolderBatchAddHostsToClusterResult from a dict
array_of_folder_batch_add_hosts_to_cluster_result_form_dict = array_of_folder_batch_add_hosts_to_cluster_result.from_dict(array_of_folder_batch_add_hosts_to_cluster_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


