# HostSgxInfoFlcModesEnum

Flexible Launch Enclave (FLC) modes.  Possible values: - `off`: Flexible Launch Enclave (FLC) is not available on the host.      The   \"launch enclave MSRs\" are initialized with Intel's public key hash. - `locked`: FLC is available and the \"launch Enclave MSRs\" are locked and   initialized with the provided public key hash. - `unlocked`: FLC is available and the \"launch enclave MSRs\" are writeable and   initialized with Intel's public key hash.    ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


