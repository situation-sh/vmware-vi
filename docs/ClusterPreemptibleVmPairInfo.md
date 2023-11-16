# ClusterPreemptibleVmPairInfo

The *ClusterPreemptibleVmPairInfo* data object contains the monitored and the preemptible VM pair in a HA-enabled cluster.  Monitored virtual machine is a desired protected virtual machine in HA-enabled cluster when it is powered on. Any failures of this VM will continue to be handled by HA based on the VM's settings in cluster.  Preemptible virtual machine is the desired protected virtual machine in HA when it is powered on. The lowest restart priority \"disabled\" *ClusterDasVmSettingsRestartPriority_enum* will be enforced for the *ClusterPreemptibleVmPairInfo.preemptibleVm*. A virtual machine can be marked as preemptible irrespective of its *powerState* but its extra configuration should identify it as preemptible.  In case of failure of *ClusterPreemptibleVmPairInfo.monitoredVm*, the *ClusterPreemptibleVmPairInfo.preemptibleVm* will be terminated. This will free up any resources associated with *ClusterPreemptibleVmPairInfo.preemptibleVm*.  In case of insufficient resources for failover of any VM in the cluster, the *ClusterPreemptibleVmPairInfo.preemptibleVm* will be terminated to free up resources.  This data object is intended for VMware use and other usage is not supported. This data object will be removed in a future release. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Server-assigned unique ID for pairs.  When adding a new pair, do not specify this property. The server will assign the key and any assigned value will be ignored.  | [optional] 
**monitored_vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**preemptible_vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.cluster_preemptible_vm_pair_info import ClusterPreemptibleVmPairInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterPreemptibleVmPairInfo from a JSON string
cluster_preemptible_vm_pair_info_instance = ClusterPreemptibleVmPairInfo.from_json(json)
# print the JSON string representation of the object
print ClusterPreemptibleVmPairInfo.to_json()

# convert the object into a dict
cluster_preemptible_vm_pair_info_dict = cluster_preemptible_vm_pair_info_instance.to_dict()
# create an instance of ClusterPreemptibleVmPairInfo from a dict
cluster_preemptible_vm_pair_info_form_dict = cluster_preemptible_vm_pair_info.from_dict(cluster_preemptible_vm_pair_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


