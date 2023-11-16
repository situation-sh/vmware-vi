# VirtualMachineHtSharingEnum

Deprecated as of vSphere API 6.7.  Set of possible values for *VirtualMachineFlagInfo.htSharing*.  Possible values: - `any`: VCPUs may freely share cores at any time with any other   VCPUs (default for all virtual machines on a hyperthreaded   system). - `none`: VCPUs should not share cores with each other or with VCPUs   from other virtual machines.      That is, each VCPU from this   virtual machine should always get a whole core to itself,   with the other logical CPU on that core being placed into   the \"halted\" state. - `internal`: Similar to \"none\", in that VCPUs from this virtual machine   will not be allowed to share cores with VCPUs from other   virtual machines.      However, other VCPUs from the same virtual   machine will be allowed to share cores together. This   configuration option is only permitted for SMP virtual   machines. If applied to a uniprocessor virtual machine, it   will be converted to the \"none\" sharing option. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


