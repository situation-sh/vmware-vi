# ArrayOfClusterPreemptibleVmPairInfo

A boxed array of *ClusterPreemptibleVmPairInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterPreemptibleVmPairInfo]**](ClusterPreemptibleVmPairInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_preemptible_vm_pair_info import ArrayOfClusterPreemptibleVmPairInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterPreemptibleVmPairInfo from a JSON string
array_of_cluster_preemptible_vm_pair_info_instance = ArrayOfClusterPreemptibleVmPairInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterPreemptibleVmPairInfo.to_json()

# convert the object into a dict
array_of_cluster_preemptible_vm_pair_info_dict = array_of_cluster_preemptible_vm_pair_info_instance.to_dict()
# create an instance of ArrayOfClusterPreemptibleVmPairInfo from a dict
array_of_cluster_preemptible_vm_pair_info_form_dict = array_of_cluster_preemptible_vm_pair_info.from_dict(array_of_cluster_preemptible_vm_pair_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


