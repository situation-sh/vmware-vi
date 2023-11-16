# HostTpmAttestationInfoAcceptanceStatus

A boxed *HostTpmAttestationInfoAcceptanceStatus_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**HostTpmAttestationInfoAcceptanceStatusEnum**](HostTpmAttestationInfoAcceptanceStatusEnum.md) |  | 

## Example

```python
from vmware_vi.models.host_tpm_attestation_info_acceptance_status import HostTpmAttestationInfoAcceptanceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of HostTpmAttestationInfoAcceptanceStatus from a JSON string
host_tpm_attestation_info_acceptance_status_instance = HostTpmAttestationInfoAcceptanceStatus.from_json(json)
# print the JSON string representation of the object
print HostTpmAttestationInfoAcceptanceStatus.to_json()

# convert the object into a dict
host_tpm_attestation_info_acceptance_status_dict = host_tpm_attestation_info_acceptance_status_instance.to_dict()
# create an instance of HostTpmAttestationInfoAcceptanceStatus from a dict
host_tpm_attestation_info_acceptance_status_form_dict = host_tpm_attestation_info_acceptance_status.from_dict(host_tpm_attestation_info_acceptance_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


