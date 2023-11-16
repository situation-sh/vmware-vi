# VirtualTPM

This data object type represents a TPM 2.0 module in a virtual machine.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endorsement_key_certificate_signing_request** | **List[bytearray]** | Endorsement Key Certificate Signing Request in DER format.  There may be more than one - one for RSA 2048, one for ECC NIST P256, and any number of other signing requests for other algorithms.  ***Since:*** vSphere API 6.7  | [optional] 
**endorsement_key_certificate** | **List[bytearray]** | Endorsement Key Certificate in DER format.  There may be more than one. Indices in this array do not match indices in *VirtualTPM.endorsementKeyCertificateSigningRequest* array, entries must be matched by comparing fields in DER data between certificate signing requests and certificates.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.virtual_tpm import VirtualTPM

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualTPM from a JSON string
virtual_tpm_instance = VirtualTPM.from_json(json)
# print the JSON string representation of the object
print VirtualTPM.to_json()

# convert the object into a dict
virtual_tpm_dict = virtual_tpm_instance.to_dict()
# create an instance of VirtualTPM from a dict
virtual_tpm_form_dict = virtual_tpm.from_dict(virtual_tpm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


