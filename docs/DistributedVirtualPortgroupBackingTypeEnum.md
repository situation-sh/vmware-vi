# DistributedVirtualPortgroupBackingTypeEnum

The *DistributedVirtualPortgroupBackingType_enum* enum defines the distributed virtual portgroup backing type.  Possible values: - `standard`: The portgroup is created by vCenter. - `nsx`: The portgroup is created by NSX manager.      For NSX backing type, We only support ephemeral portgroup type.   If *DistributedVirtualPortgroupPortgroupType_enum* is   ephemeral, A *DistributedVirtualPort* will be   dynamicly created by NSX when the virtual machine is reconfigured   to connect to the portgroup.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


