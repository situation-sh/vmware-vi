# FolderBatchAddHostsToClusterResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts_added_to_cluster** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of hosts that were successfully added to the cluster in the desired state.  ***Since:*** vSphere API 6.7.1  Refers instances of *HostSystem*.  | [optional] 
**hosts_failed_inventory_add** | [**List[FolderFailedHostResult]**](FolderFailedHostResult.md) | Contains a fault for each host that failed addition to the inventory.  A failed host will not be part of hostsAddedToCluster list.  ***Since:*** vSphere API 6.7.1  | [optional] 
**hosts_failed_move_to_cluster** | [**List[FolderFailedHostResult]**](FolderFailedHostResult.md) | List of hosts that are part of inventory but failed to move to the cluster in the desired state.  A failed host will not be part of hostsAddedToCluster list however, a failed host will be part of inventory as it might have been added as a standalone host but failed to move to cluster in the desired state.  ***Since:*** vSphere API 6.7.1  | [optional] 

## Example

```python
from vmware_vi.models.folder_batch_add_hosts_to_cluster_result import FolderBatchAddHostsToClusterResult

# TODO update the JSON string below
json = "{}"
# create an instance of FolderBatchAddHostsToClusterResult from a JSON string
folder_batch_add_hosts_to_cluster_result_instance = FolderBatchAddHostsToClusterResult.from_json(json)
# print the JSON string representation of the object
print FolderBatchAddHostsToClusterResult.to_json()

# convert the object into a dict
folder_batch_add_hosts_to_cluster_result_dict = folder_batch_add_hosts_to_cluster_result_instance.to_dict()
# create an instance of FolderBatchAddHostsToClusterResult from a dict
folder_batch_add_hosts_to_cluster_result_form_dict = folder_batch_add_hosts_to_cluster_result.from_dict(folder_batch_add_hosts_to_cluster_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


