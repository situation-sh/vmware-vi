# ArrayOfClusterComputeResourceClusterConfigResult

A boxed array of *ClusterComputeResourceClusterConfigResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterComputeResourceClusterConfigResult]**](ClusterComputeResourceClusterConfigResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_compute_resource_cluster_config_result import ArrayOfClusterComputeResourceClusterConfigResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterComputeResourceClusterConfigResult from a JSON string
array_of_cluster_compute_resource_cluster_config_result_instance = ArrayOfClusterComputeResourceClusterConfigResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterComputeResourceClusterConfigResult.to_json()

# convert the object into a dict
array_of_cluster_compute_resource_cluster_config_result_dict = array_of_cluster_compute_resource_cluster_config_result_instance.to_dict()
# create an instance of ArrayOfClusterComputeResourceClusterConfigResult from a dict
array_of_cluster_compute_resource_cluster_config_result_form_dict = array_of_cluster_compute_resource_cluster_config_result.from_dict(array_of_cluster_compute_resource_cluster_config_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


