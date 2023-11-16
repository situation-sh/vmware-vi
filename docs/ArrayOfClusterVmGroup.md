# ArrayOfClusterVmGroup

A boxed array of *ClusterVmGroup*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterVmGroup]**](ClusterVmGroup.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_vm_group import ArrayOfClusterVmGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterVmGroup from a JSON string
array_of_cluster_vm_group_instance = ArrayOfClusterVmGroup.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterVmGroup.to_json()

# convert the object into a dict
array_of_cluster_vm_group_dict = array_of_cluster_vm_group_instance.to_dict()
# create an instance of ArrayOfClusterVmGroup from a dict
array_of_cluster_vm_group_form_dict = array_of_cluster_vm_group.from_dict(array_of_cluster_vm_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


