# VAppCloneSpecProvisioningTypeEnum

The cloned VMs can either be provisioned the same way as the VMs they are a clone of, thin provisioned or thick provisioned, or linked clones (i.e., using delta disks).  Possible values: - `sameAsSource`: Each disk in the cloned virtual machines will have the same   type of disk as the source vApp. - `thin`: Each disk in the cloned virtual machines is allocated in full   size now and committed on demand.      This is only supported on   VMFS-3 and newer datastores. Other types of datastores may   create thick disks. - `thick`: Each disk in the cloned virtual machines are allocated and   committed in full size immediately.    ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


