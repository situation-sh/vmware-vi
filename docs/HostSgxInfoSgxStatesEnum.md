# HostSgxInfoSgxStatesEnum

Host SGX states.  Possible values: - `notPresent`: SGX is not present in the CPU. - `disabledBIOS`: SGX is disabled in the BIOS. - `disabledCFW101`: SGX is disabled because CPU erratum CFW101 is present. - `disabledCPUMismatch`: SGX is disabled due to a mismatch in the SGX capabilities   exposed by different CPUs. - `disabledNoFLC`: SGX is disabled because the CPU does not support FLC. - `disabledNUMAUnsup`: SGX is disabled because the host uses NUMA, which is not   supported with SGX. - `disabledMaxEPCRegs`: SGX is disabled because the host exceeds the maximum supported   number of EPC regions. - `enabled`: SGX is enabled.    ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


