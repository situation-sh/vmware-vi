# GenerateCertificateSigningRequestByDnRequestType

The parameters of *HostCertificateManager.GenerateCertificateSigningRequestByDn*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distinguished_name** | **str** | DN to be used as subject in CSR.  | 
**spec** | [**HostCertificateManagerCertificateSpec**](HostCertificateManagerCertificateSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.generate_certificate_signing_request_by_dn_request_type import GenerateCertificateSigningRequestByDnRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateCertificateSigningRequestByDnRequestType from a JSON string
generate_certificate_signing_request_by_dn_request_type_instance = GenerateCertificateSigningRequestByDnRequestType.from_json(json)
# print the JSON string representation of the object
print GenerateCertificateSigningRequestByDnRequestType.to_json()

# convert the object into a dict
generate_certificate_signing_request_by_dn_request_type_dict = generate_certificate_signing_request_by_dn_request_type_instance.to_dict()
# create an instance of GenerateCertificateSigningRequestByDnRequestType from a dict
generate_certificate_signing_request_by_dn_request_type_form_dict = generate_certificate_signing_request_by_dn_request_type.from_dict(generate_certificate_signing_request_by_dn_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


