# ArrayOfClusterVmReadiness

A boxed array of *ClusterVmReadiness*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterVmReadiness]**](ClusterVmReadiness.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_vm_readiness import ArrayOfClusterVmReadiness

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterVmReadiness from a JSON string
array_of_cluster_vm_readiness_instance = ArrayOfClusterVmReadiness.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterVmReadiness.to_json()

# convert the object into a dict
array_of_cluster_vm_readiness_dict = array_of_cluster_vm_readiness_instance.to_dict()
# create an instance of ArrayOfClusterVmReadiness from a dict
array_of_cluster_vm_readiness_form_dict = array_of_cluster_vm_readiness.from_dict(array_of_cluster_vm_readiness_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


