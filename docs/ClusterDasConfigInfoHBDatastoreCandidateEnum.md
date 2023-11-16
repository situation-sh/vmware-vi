# ClusterDasConfigInfoHBDatastoreCandidateEnum

The policy to determine the candidates from which vCenter Server can choose heartbeat datastores.  Possible values: - `userSelectedDs`: vCenter Server chooses heartbeat datastores from the set specified   by the user (see *ClusterDasConfigInfo.heartbeatDatastore*).      More specifically,   datastores not included in the set will not be chosen. Note that if   *ClusterDasConfigInfo.heartbeatDatastore* is empty, datastore heartbeating will   be disabled for HA. - `allFeasibleDs`: vCenter Server chooses heartbeat datastores from all the feasible ones,   i.e., the datastores that are accessible to more than one host in   the cluster.      The choice will be made without giving preference to those   specified by the user (see *ClusterDasConfigInfo.heartbeatDatastore*). - `allFeasibleDsWithUserPreference`: vCenter Server chooses heartbeat datastores from all the feasible ones   while giving preference to those specified by the user (see *ClusterDasConfigInfo.heartbeatDatastore*).      More specifically, the datastores not included in *ClusterDasConfigInfo.heartbeatDatastore* will be   chosen if and only if the specified ones are not sufficient.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


