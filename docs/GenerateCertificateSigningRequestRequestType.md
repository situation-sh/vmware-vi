# GenerateCertificateSigningRequestRequestType

The parameters of *HostCertificateManager.GenerateCertificateSigningRequest*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_ip_address_as_common_name** | **bool** | if true, use host&#39;s management IP address as CN in the CSR; otherwise use host&#39;s FQDN.  | 
**spec** | [**HostCertificateManagerCertificateSpec**](HostCertificateManagerCertificateSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.generate_certificate_signing_request_request_type import GenerateCertificateSigningRequestRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateCertificateSigningRequestRequestType from a JSON string
generate_certificate_signing_request_request_type_instance = GenerateCertificateSigningRequestRequestType.from_json(json)
# print the JSON string representation of the object
print GenerateCertificateSigningRequestRequestType.to_json()

# convert the object into a dict
generate_certificate_signing_request_request_type_dict = generate_certificate_signing_request_request_type_instance.to_dict()
# create an instance of GenerateCertificateSigningRequestRequestType from a dict
generate_certificate_signing_request_request_type_form_dict = generate_certificate_signing_request_request_type.from_dict(generate_certificate_signing_request_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


