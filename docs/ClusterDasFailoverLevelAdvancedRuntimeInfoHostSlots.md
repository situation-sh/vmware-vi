# ClusterDasFailoverLevelAdvancedRuntimeInfoHostSlots


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**slots** | **int** | The number of slots in this host.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.cluster_das_failover_level_advanced_runtime_info_host_slots import ClusterDasFailoverLevelAdvancedRuntimeInfoHostSlots

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasFailoverLevelAdvancedRuntimeInfoHostSlots from a JSON string
cluster_das_failover_level_advanced_runtime_info_host_slots_instance = ClusterDasFailoverLevelAdvancedRuntimeInfoHostSlots.from_json(json)
# print the JSON string representation of the object
print ClusterDasFailoverLevelAdvancedRuntimeInfoHostSlots.to_json()

# convert the object into a dict
cluster_das_failover_level_advanced_runtime_info_host_slots_dict = cluster_das_failover_level_advanced_runtime_info_host_slots_instance.to_dict()
# create an instance of ClusterDasFailoverLevelAdvancedRuntimeInfoHostSlots from a dict
cluster_das_failover_level_advanced_runtime_info_host_slots_form_dict = cluster_das_failover_level_advanced_runtime_info_host_slots.from_dict(cluster_das_failover_level_advanced_runtime_info_host_slots_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


