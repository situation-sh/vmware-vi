# ArrayOfClusterOrchestrationInfo

A boxed array of *ClusterOrchestrationInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterOrchestrationInfo]**](ClusterOrchestrationInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_orchestration_info import ArrayOfClusterOrchestrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterOrchestrationInfo from a JSON string
array_of_cluster_orchestration_info_instance = ArrayOfClusterOrchestrationInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterOrchestrationInfo.to_json()

# convert the object into a dict
array_of_cluster_orchestration_info_dict = array_of_cluster_orchestration_info_instance.to_dict()
# create an instance of ArrayOfClusterOrchestrationInfo from a dict
array_of_cluster_orchestration_info_form_dict = array_of_cluster_orchestration_info.from_dict(array_of_cluster_orchestration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


