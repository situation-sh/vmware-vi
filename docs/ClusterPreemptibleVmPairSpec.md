# ClusterPreemptibleVmPairSpec

Provides monitored and preemptible VM pair along with any of the operations (add, edit or remove) to append, modify or remove this pair info from *ClusterPreemptibleVmPairInfo* list.  This data object is intended for VMware use and other usage is not supported. This data object will be removed in a future release. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**ClusterPreemptibleVmPairInfo**](ClusterPreemptibleVmPairInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_preemptible_vm_pair_spec import ClusterPreemptibleVmPairSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterPreemptibleVmPairSpec from a JSON string
cluster_preemptible_vm_pair_spec_instance = ClusterPreemptibleVmPairSpec.from_json(json)
# print the JSON string representation of the object
print ClusterPreemptibleVmPairSpec.to_json()

# convert the object into a dict
cluster_preemptible_vm_pair_spec_dict = cluster_preemptible_vm_pair_spec_instance.to_dict()
# create an instance of ClusterPreemptibleVmPairSpec from a dict
cluster_preemptible_vm_pair_spec_form_dict = cluster_preemptible_vm_pair_spec.from_dict(cluster_preemptible_vm_pair_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


