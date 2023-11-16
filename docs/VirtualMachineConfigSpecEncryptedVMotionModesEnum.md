# VirtualMachineConfigSpecEncryptedVMotionModesEnum

The set of valid encrypted vMotion modes for a VM.  If the VM is encrypted, its encrypted vMotion mode will be required.  Possible values: - `disabled`: Do not use encrypted vMotion, even if available. - `opportunistic`: Use encrypted vMotion if source and destination hosts support it,   fall back to unencrypted vMotion otherwise.      This is the default option. - `required`: Allow only encrypted vMotion.      If the source or destination host does   not support vMotion encryption, do not allow the vMotion to occur.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


