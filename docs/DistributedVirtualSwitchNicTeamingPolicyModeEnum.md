# DistributedVirtualSwitchNicTeamingPolicyModeEnum

List of possible teaming modes supported by the vNetwork Distributed Switch.  The different policy modes define the way traffic is routed through the different uplink ports in a team.  Possible values: - `loadbalance_ip`: Routing based on IP hash - `loadbalance_srcmac`: Route based on source MAC hash - `loadbalance_srcid`: Route based on the source of the port ID - `failover_explicit`: Use explicit failover order - `loadbalance_loadbased`: Routing based by dynamically balancing traffic through the NICs   in a team.      This is the recommended teaming policy when the   network I/O control feature is enabled for the vNetwork   Distributed Switch.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


