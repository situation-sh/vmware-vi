# VMwareDVSTeamingMatchStatusEnum

The teaming health check match status.  Possible values: - `iphashMatch`: The value of 'loadbalance\\_ip' is used in a uplink teaming policy   *VmwareUplinkPortTeamingPolicy.policy*   in the vSphere Distributed Switch, and the external physical switch   has the matching EtherChannel configuration. - `nonIphashMatch`: The value of 'loadbalance\\_ip' is not used in a uplink teaming policy   *VmwareUplinkPortTeamingPolicy.policy*   in the vSphere Distributed Switch, and the external physical switch   does not have EtherChannel configuration. - `iphashMismatch`: The value of 'loadbalance\\_ip' is used in a uplink teaming policy   *VmwareUplinkPortTeamingPolicy.policy*   in the vSphere Distributed Switch, but the external physical switch   does not have the matching EtherChannel configuration. - `nonIphashMismatch`: The value of 'loadbalance\\_ip' is not used in a uplink teaming policy   *VmwareUplinkPortTeamingPolicy.policy*   in the vSphere Distributed Switch, but the external physical switch   has EtherChannel configuration.    ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


