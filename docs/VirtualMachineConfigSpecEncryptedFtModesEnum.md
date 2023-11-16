# VirtualMachineConfigSpecEncryptedFtModesEnum

The set of valid encrypted Fault Tolerance modes for a VM.  If the VM is encrypted, its encrypted Fault Tolerance mode will be required.  Possible values: - `ftEncryptionDisabled`: Do not use encrypted Fault Tolerance, even if available. - `ftEncryptionOpportunistic`: Use encrypted Fault Tolerance if source and destination hosts   support it, fall back to unencrypted Fault Tolerance otherwise.      This is the default option. - `ftEncryptionRequired`: Allow only encrypted Fault Tolerance.      If either the source or   destination host does not support encrypted Fault Tolerance,   do not allow the Fault Tolerance to occur.  ***Since:*** vSphere API 7.0.2.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


