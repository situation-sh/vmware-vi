# ArrayOfClusterVmOrchestrationInfo

A boxed array of *ClusterVmOrchestrationInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterVmOrchestrationInfo]**](ClusterVmOrchestrationInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_vm_orchestration_info import ArrayOfClusterVmOrchestrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterVmOrchestrationInfo from a JSON string
array_of_cluster_vm_orchestration_info_instance = ArrayOfClusterVmOrchestrationInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterVmOrchestrationInfo.to_json()

# convert the object into a dict
array_of_cluster_vm_orchestration_info_dict = array_of_cluster_vm_orchestration_info_instance.to_dict()
# create an instance of ArrayOfClusterVmOrchestrationInfo from a dict
array_of_cluster_vm_orchestration_info_form_dict = array_of_cluster_vm_orchestration_info.from_dict(array_of_cluster_vm_orchestration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


