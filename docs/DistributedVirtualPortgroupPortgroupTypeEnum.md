# DistributedVirtualPortgroupPortgroupTypeEnum

The *DistributedVirtualPortgroupPortgroupType_enum* enum defines the distributed virtual portgroup types (*DistributedVirtualPortgroup*.*DistributedVirtualPortgroup.config*.*DVPortgroupConfigInfo.type*).  Early binding specifies a static set of ports that are created when you create the distributed virtual portgroup. An ephemeral portgroup uses dynamic ports that are created when you power on a virtual machine.  Possible values: - `earlyBinding`: A free *DistributedVirtualPort* will be selected and assigned to   a *VirtualMachine* when the virtual machine is reconfigured to   connect to the portgroup. - `lateBinding`:       Deprecated as of vSphere API 5.0.      A free *DistributedVirtualPort* will be selected and   assigned to a *VirtualMachine* when the virtual machine is   powered on. - `ephemeral`: A *DistributedVirtualPort* will be created and assigned to a   *VirtualMachine* when the virtual machine is powered on, and will   be deleted when the virtual machine is powered off.      An ephemeral portgroup has   no limit on the number of ports that can be a part of this portgroup.   In cases where the vCenter Server is unavailable the host can   create conflict ports in this portgroup to be used by a virtual machine   at power on.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


