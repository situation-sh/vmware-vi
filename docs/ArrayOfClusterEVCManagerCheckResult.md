# ArrayOfClusterEVCManagerCheckResult

A boxed array of *ClusterEVCManagerCheckResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterEVCManagerCheckResult]**](ClusterEVCManagerCheckResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_evc_manager_check_result import ArrayOfClusterEVCManagerCheckResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterEVCManagerCheckResult from a JSON string
array_of_cluster_evc_manager_check_result_instance = ArrayOfClusterEVCManagerCheckResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterEVCManagerCheckResult.to_json()

# convert the object into a dict
array_of_cluster_evc_manager_check_result_dict = array_of_cluster_evc_manager_check_result_instance.to_dict()
# create an instance of ArrayOfClusterEVCManagerCheckResult from a dict
array_of_cluster_evc_manager_check_result_form_dict = array_of_cluster_evc_manager_check_result.from_dict(array_of_cluster_evc_manager_check_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


