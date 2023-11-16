# QuarantineModeFaultFaultTypeEnum

Possible values: - `NoCompatibleNonQuarantinedHost`: The cluster does not contain any non-quarantined host satisfying the   VM/host affinity rules for the VM. - `CorrectionDisallowed`: The current DRS migration priority setting disallows generating a   recommendation to prevent VMs on quarantined hosts.      Thus, the   violation will not be corrected. - `CorrectionImpact`: DRS has determined that evacuation of VMs from quarantined hosts   impacts respecting cluster constraints or performance goals so they   are not evacuated.    ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


