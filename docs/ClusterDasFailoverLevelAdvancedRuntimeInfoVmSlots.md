# ClusterDasFailoverLevelAdvancedRuntimeInfoVmSlots


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**slots** | **int** | The number of slots required by this virtual machine  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.cluster_das_failover_level_advanced_runtime_info_vm_slots import ClusterDasFailoverLevelAdvancedRuntimeInfoVmSlots

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasFailoverLevelAdvancedRuntimeInfoVmSlots from a JSON string
cluster_das_failover_level_advanced_runtime_info_vm_slots_instance = ClusterDasFailoverLevelAdvancedRuntimeInfoVmSlots.from_json(json)
# print the JSON string representation of the object
print ClusterDasFailoverLevelAdvancedRuntimeInfoVmSlots.to_json()

# convert the object into a dict
cluster_das_failover_level_advanced_runtime_info_vm_slots_dict = cluster_das_failover_level_advanced_runtime_info_vm_slots_instance.to_dict()
# create an instance of ClusterDasFailoverLevelAdvancedRuntimeInfoVmSlots from a dict
cluster_das_failover_level_advanced_runtime_info_vm_slots_form_dict = cluster_das_failover_level_advanced_runtime_info_vm_slots.from_dict(cluster_das_failover_level_advanced_runtime_info_vm_slots_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


