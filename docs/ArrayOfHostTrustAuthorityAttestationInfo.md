# ArrayOfHostTrustAuthorityAttestationInfo

A boxed array of *HostTrustAuthorityAttestationInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostTrustAuthorityAttestationInfo]**](HostTrustAuthorityAttestationInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_trust_authority_attestation_info import ArrayOfHostTrustAuthorityAttestationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostTrustAuthorityAttestationInfo from a JSON string
array_of_host_trust_authority_attestation_info_instance = ArrayOfHostTrustAuthorityAttestationInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostTrustAuthorityAttestationInfo.to_json()

# convert the object into a dict
array_of_host_trust_authority_attestation_info_dict = array_of_host_trust_authority_attestation_info_instance.to_dict()
# create an instance of ArrayOfHostTrustAuthorityAttestationInfo from a dict
array_of_host_trust_authority_attestation_info_form_dict = array_of_host_trust_authority_attestation_info.from_dict(array_of_host_trust_authority_attestation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


