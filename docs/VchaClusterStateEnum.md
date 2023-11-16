# VchaClusterStateEnum

VchaClusterState enum defines the possible states for a VCHA Cluster.  Possible values: - `healthy`: All three nodes in a VCHA Cluster are healthy and connected.      State   replication between Active and Passive node is working and both   nodes are in sync. - `degraded`: A VCHA Cluster is said to be in a degraded state for   either or all of the following reasons:   \\- There is a node loss.      \\- State replication between the Active and Passive node fails. - `isolated`: All three nodes are isolated from each other.    ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


