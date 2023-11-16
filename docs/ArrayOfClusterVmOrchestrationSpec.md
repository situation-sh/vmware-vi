# ArrayOfClusterVmOrchestrationSpec

A boxed array of *ClusterVmOrchestrationSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterVmOrchestrationSpec]**](ClusterVmOrchestrationSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_vm_orchestration_spec import ArrayOfClusterVmOrchestrationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterVmOrchestrationSpec from a JSON string
array_of_cluster_vm_orchestration_spec_instance = ArrayOfClusterVmOrchestrationSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterVmOrchestrationSpec.to_json()

# convert the object into a dict
array_of_cluster_vm_orchestration_spec_dict = array_of_cluster_vm_orchestration_spec_instance.to_dict()
# create an instance of ArrayOfClusterVmOrchestrationSpec from a dict
array_of_cluster_vm_orchestration_spec_form_dict = array_of_cluster_vm_orchestration_spec.from_dict(array_of_cluster_vm_orchestration_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


