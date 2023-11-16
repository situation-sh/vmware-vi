# ScsiLunVStorageSupportStatusEnum

Storage array hardware acceleration support status.  When a host boots, the support status is unknown. As a host attempts hardware-accelerated operations, it determines whether the storage device supports hardware acceleration and sets the *ScsiLun.vStorageSupport* property accordingly.  Possible values: - `vStorageSupported`: Storage device supports hardware acceleration.      The ESX host will use the feature to offload certain   storage-related operations to the device. - `vStorageUnsupported`: Storage device does not support hardware acceleration.      The ESX host will handle all storage-related operations. - `vStorageUnknown`: Initial support status value.    ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


