# VAppIPAssignmentInfoIpAllocationPolicyEnum

IP allocation policy for a deployment.  Possible values: - `dhcpPolicy`: Specifies that DHCP must be used to allocate IP addresses to the vApp - `transientPolicy`: Specifies that IP allocation is done through the range managed by the   vSphere platform.      The IP addresses are allocated when needed, typically at   power-on, and deallocated during power-off. There is no guarantee that a   vApp will get the same IP address when restarted. - `fixedPolicy`: Specifies that IP addresses are configured manually when the vApp is deployed   and will be kept until reconfigured or the vApp destroyed.      This will ensure   that a vApp gets a consistent IP for its life-time. - `fixedAllocatedPolicy`: Specifies that IP allocation is done through the range managed by the VI   platform.      The IP addresses are allocated at first power-on, and remain   allocated at power-off. This will ensure that a vApp gets a consistent   IP for its life-time.      ***Since:*** vSphere API 5.1  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


