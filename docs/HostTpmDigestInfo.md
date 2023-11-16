# HostTpmDigestInfo

This data object type describes the digest values in the Platform Configuration Register (PCR) of a Trusted Platform Module (TPM) device.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pcr_number** | **int** | Index of the PCR that stores the TPM digest value.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.host_tpm_digest_info import HostTpmDigestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostTpmDigestInfo from a JSON string
host_tpm_digest_info_instance = HostTpmDigestInfo.from_json(json)
# print the JSON string representation of the object
print HostTpmDigestInfo.to_json()

# convert the object into a dict
host_tpm_digest_info_dict = host_tpm_digest_info_instance.to_dict()
# create an instance of HostTpmDigestInfo from a dict
host_tpm_digest_info_form_dict = host_tpm_digest_info.from_dict(host_tpm_digest_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


