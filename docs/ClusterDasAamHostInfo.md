# ClusterDasAamHostInfo

Deprecated as of vSphere API 5.0, this object is no longer returned by vCenter Server. Availability information is now reported using *HostRuntimeInfo.dasHostState*.  The *ClusterDasAamHostInfo* object contains a list of the ESX hosts in an HA cluster and a list that identifies the _primary_ hosts.  (AAM is a component of the HA service.) The primary hosts share the joint responsibility of maintaining all cluster state and one will initiate failover actions should a failure occur.  When you add an ESX host to a vSphere HA cluster, the host downloads HA agent components from the vCenter Server. The HA agent maintains communication with the vCenter Server.  When the host downloads the HA agent, the host configures the agent to communicate with other agents in the cluster. A host that joins the cluster communicates with an existing primary host to complete its configuration (except when you are adding the first host to the cluster). - The first five hosts added to the cluster are designated   as primary hosts. All subsequent hosts are designated as secondary hosts. - If a primary host is removed from the cluster,   the vCenter Server promotes another host to primary status. - There must be at least one functional primary host for vSphere HA   to operate correctly. If there is not an available primary host   (no response), host configuration for HA will fail.   If there is a total cluster failure, HA will begin restarting virtual   machines as soon as one host recovers and its HA agent is up and running.    One of the primary hosts assumes the role of the active primary host. The active primary host responsibilities include the following activities: - Decides where to restart virtual machines. - Tracks failed restart attempts. - Determines when it is appropriate to continue attempts to restart   a virtual machine.    If the active primary host fails, another primary host replaces it.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_das_state** | [**List[ClusterDasAamNodeState]**](ClusterDasAamNodeState.md) | The state of HA on the hosts.  ***Since:*** vSphere API 4.0  | [optional] 
**primary_hosts** | **List[str]** | The list of primary hosts.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_das_aam_host_info import ClusterDasAamHostInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasAamHostInfo from a JSON string
cluster_das_aam_host_info_instance = ClusterDasAamHostInfo.from_json(json)
# print the JSON string representation of the object
print ClusterDasAamHostInfo.to_json()

# convert the object into a dict
cluster_das_aam_host_info_dict = cluster_das_aam_host_info_instance.to_dict()
# create an instance of ClusterDasAamHostInfo from a dict
cluster_das_aam_host_info_form_dict = cluster_das_aam_host_info.from_dict(cluster_das_aam_host_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


