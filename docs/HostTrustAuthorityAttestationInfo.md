# HostTrustAuthorityAttestationInfo

This data object type represents result of the attestation done by Trust Authority attestation service.  ***Since:*** vSphere API 7.0.1.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attestation_status** | **str** | Status of the attestation.  See *HostTrustAuthorityAttestationInfoAttestationStatus_enum* for the supported values.  ***Since:*** vSphere API 7.0.1.0  | 
**service_id** | **str** | ID of the attestation service in case of attestation success.  Unset when not attested.  ***Since:*** vSphere API 7.0.1.0  | [optional] 
**attested_at** | **datetime** | Time of attestation.  ***Since:*** vSphere API 7.0.1.0  | [optional] 
**attested_until** | **datetime** | Time until attestation is valid.  ***Since:*** vSphere API 7.0.1.0  | [optional] 
**messages** | [**List[LocalizableMessage]**](LocalizableMessage.md) | Messages explaining attestation failure or attestation status retrieval errors, if any.  ***Since:*** vSphere API 7.0.1.0  | [optional] 

## Example

```python
from vmware_vi.models.host_trust_authority_attestation_info import HostTrustAuthorityAttestationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostTrustAuthorityAttestationInfo from a JSON string
host_trust_authority_attestation_info_instance = HostTrustAuthorityAttestationInfo.from_json(json)
# print the JSON string representation of the object
print HostTrustAuthorityAttestationInfo.to_json()

# convert the object into a dict
host_trust_authority_attestation_info_dict = host_trust_authority_attestation_info_instance.to_dict()
# create an instance of HostTrustAuthorityAttestationInfo from a dict
host_trust_authority_attestation_info_form_dict = host_trust_authority_attestation_info.from_dict(host_trust_authority_attestation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


