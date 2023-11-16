# ArrayOfHostTpmAttestationInfo

A boxed array of *HostTpmAttestationInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostTpmAttestationInfo]**](HostTpmAttestationInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_tpm_attestation_info import ArrayOfHostTpmAttestationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostTpmAttestationInfo from a JSON string
array_of_host_tpm_attestation_info_instance = ArrayOfHostTpmAttestationInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostTpmAttestationInfo.to_json()

# convert the object into a dict
array_of_host_tpm_attestation_info_dict = array_of_host_tpm_attestation_info_instance.to_dict()
# create an instance of ArrayOfHostTpmAttestationInfo from a dict
array_of_host_tpm_attestation_info_form_dict = array_of_host_tpm_attestation_info.from_dict(array_of_host_tpm_attestation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


