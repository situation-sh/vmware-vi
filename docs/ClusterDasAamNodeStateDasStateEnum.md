# ClusterDasAamNodeStateDasStateEnum

The *ClusterDasAamNodeStateDasState_enum* enumerated type defines values for host HA configuration and runtime state properties (*ClusterDasAamNodeState.configState* and *ClusterDasAamNodeState.runtimeState*).  Possible values: - `uninitialized`: HA has never been enabled on the the host. - `initialized`: HA agents have been installed but are not running on the the host. - `configuring`: HA configuration is in progress. - `unconfiguring`: HA configuration is being removed. - `running`: HA agent is running on this host. - `error`: There is an error condition.      This can represent a configuration   error or a host agent runtime error. - `agentShutdown`: The HA agent has been shut down. - `nodeFailed`: The host is not reachable.      This can represent a host failure   or an isolated host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


