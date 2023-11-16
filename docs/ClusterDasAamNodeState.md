# ClusterDasAamNodeState

Deprecated as of vSphere API 5.0, this object is no longer returned by vCenter Server. See *HostRuntimeInfo.dasHostState* for a description of the objects now used.  The *ClusterDasAamNodeState* data object represents the state of the HA service on an ESX host.  (AAM is a component of this service.)  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**name** | **str** | Name of the host (*HostSystem*.*ManagedEntity.name*).  ***Since:*** vSphere API 4.0  | 
**config_state** | **str** | Configuration state of the HA agent on the host.  The property can be one of the following values:  configuring   error   unconfiguring   running    &lt;code&gt;configState&lt;/code&gt; represents setting or resetting the HA configuration on the host. If the configuration operation is successful, the value of &lt;code&gt;configState&lt;/code&gt; changes to &lt;code&gt;running&lt;/code&gt;. See *ClusterDasAamNodeStateDasState_enum*.  ***Since:*** vSphere API 4.0  | 
**runtime_state** | **str** | The runtime state of the HA agent on the node.  The property can be one of the following values:  uninitialized   initialized   running   error   agentShutdown   nodeFailed  See *ClusterDasAamNodeStateDasState_enum*.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.cluster_das_aam_node_state import ClusterDasAamNodeState

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasAamNodeState from a JSON string
cluster_das_aam_node_state_instance = ClusterDasAamNodeState.from_json(json)
# print the JSON string representation of the object
print ClusterDasAamNodeState.to_json()

# convert the object into a dict
cluster_das_aam_node_state_dict = cluster_das_aam_node_state_instance.to_dict()
# create an instance of ClusterDasAamNodeState from a dict
cluster_das_aam_node_state_form_dict = cluster_das_aam_node_state.from_dict(cluster_das_aam_node_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


