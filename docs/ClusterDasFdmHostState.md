# ClusterDasFdmHostState

The *ClusterDasFdmHostState* data object describes the availability state of each active host in a vSphere HA enabled cluster.  In a vSphere HA cluster, the active hosts form a fault domain. A host is inactive if it is in standby or maintenance mode, or it has been disconnected from vCenter Server. A vSphere HA agent, called the Fault Domain Manager (FDM), runs on each host in the fault domain.  One FDM serves as the master and the remaining FDMs as its slaves. The master is responsible for monitoring the availability of the hosts and VMs in the cluster, and restarting any VMs that fail due to a host failure or non-user-initiated power offs. The master is also responsible for reporting fault-domain state to vCenter Server.  The master FDM is determined through election by the FDMs that are alive at the time. An election occurs in the following circumstances: - When the vSphere HA feature is enabled for the cluster. - When the master's host fails. - When the management network is partitioned. In a network partition   there will be a master for each partition. However, only one master   will be responsible for a given VM. When the partition is   resolved, all but one of the masters will abdicate. - After a host in a vSphere HA cluster powers back up following a failure   that caused all hosts in the cluster to power off.    The slaves are responsible for reporting state updates to the master and restarting VMs as required. All FDMs provide the VM/Application Health Monitoring Service.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The Availability State of a host based on information reported by the entity given by the *ClusterDasFdmHostState.stateReporter* property.  See *ClusterDasFdmAvailabilityState_enum* for the set of states.  ***Since:*** vSphere API 5.0  | 
**state_reporter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_das_fdm_host_state import ClusterDasFdmHostState

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasFdmHostState from a JSON string
cluster_das_fdm_host_state_instance = ClusterDasFdmHostState.from_json(json)
# print the JSON string representation of the object
print ClusterDasFdmHostState.to_json()

# convert the object into a dict
cluster_das_fdm_host_state_dict = cluster_das_fdm_host_state_instance.to_dict()
# create an instance of ClusterDasFdmHostState from a dict
cluster_das_fdm_host_state_form_dict = cluster_das_fdm_host_state.from_dict(cluster_das_fdm_host_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


