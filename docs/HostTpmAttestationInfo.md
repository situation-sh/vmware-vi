# HostTpmAttestationInfo

This data object type represents result of TPM attestation.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **datetime** | Time of TPM attestation.  ***Since:*** vSphere API 6.7  | 
**status** | [**HostTpmAttestationInfoAcceptanceStatusEnum**](HostTpmAttestationInfoAcceptanceStatusEnum.md) |  | 
**message** | [**LocalizableMessage**](LocalizableMessage.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_tpm_attestation_info import HostTpmAttestationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostTpmAttestationInfo from a JSON string
host_tpm_attestation_info_instance = HostTpmAttestationInfo.from_json(json)
# print the JSON string representation of the object
print HostTpmAttestationInfo.to_json()

# convert the object into a dict
host_tpm_attestation_info_dict = host_tpm_attestation_info_instance.to_dict()
# create an instance of HostTpmAttestationInfo from a dict
host_tpm_attestation_info_form_dict = host_tpm_attestation_info.from_dict(host_tpm_attestation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


