# ReplaceCACertificatesAndCRLsRequestType

The parameters of *HostCertificateManager.ReplaceCACertificatesAndCRLs*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert** | **List[str]** | List of SSL certificates, in PEM format, of all CAs that should be trusted  | 
**ca_crl** | **List[str]** | List of SSL CRLs, in PEM format, issued by trusted CAs from the above list  | [optional] 

## Example

```python
from vmware_vi.models.replace_ca_certificates_and_crls_request_type import ReplaceCACertificatesAndCRLsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReplaceCACertificatesAndCRLsRequestType from a JSON string
replace_ca_certificates_and_crls_request_type_instance = ReplaceCACertificatesAndCRLsRequestType.from_json(json)
# print the JSON string representation of the object
print ReplaceCACertificatesAndCRLsRequestType.to_json()

# convert the object into a dict
replace_ca_certificates_and_crls_request_type_dict = replace_ca_certificates_and_crls_request_type_instance.to_dict()
# create an instance of ReplaceCACertificatesAndCRLsRequestType from a dict
replace_ca_certificates_and_crls_request_type_form_dict = replace_ca_certificates_and_crls_request_type.from_dict(replace_ca_certificates_and_crls_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


