# CheckTestTypeEnum

The types of tests which can requested by any of the methods in either *VirtualMachineCompatibilityChecker* or *VirtualMachineProvisioningChecker*.  Possible values: - `sourceTests`: Tests that examine only the configuration   of the virtual machine and its current host; the destination   resource pool and host or cluster are irrelevant. - `hostTests`: Tests that examine both the virtual   machine and the destination host or cluster; the destination   resource pool is irrelevant.      This set excludes tests that fall   into the datastoreTests group. - `resourcePoolTests`: Tests that check that the destination resource   pool can support the virtual machine if it is powered on.      The   destination host or cluster is relevant because it will affect the   amount of overhead memory required to run the virtual machine. - `datastoreTests`: Tests that check that the   destination host or cluster can see the datastores where the virtual   machine's virtual disks are going to be located.      The destination   resource pool is irrelevant. - `networkTests`: Tests that check that the   destination host or cluster can see the networks that the virtual   machine's virtual nic devices are going to be connected.      ***Since:*** vSphere API 5.5  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


