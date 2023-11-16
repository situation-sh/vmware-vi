# UpdateKmsSignedCsrClientCertRequestType

The parameters of *CryptoManagerKmip.UpdateKmsSignedCsrClientCert*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**KeyProviderId**](KeyProviderId.md) |  | 
**certificate** | **str** | \\[in\\] Client certificate.  | 

## Example

```python
from vmware_vi.models.update_kms_signed_csr_client_cert_request_type import UpdateKmsSignedCsrClientCertRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKmsSignedCsrClientCertRequestType from a JSON string
update_kms_signed_csr_client_cert_request_type_instance = UpdateKmsSignedCsrClientCertRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateKmsSignedCsrClientCertRequestType.to_json()

# convert the object into a dict
update_kms_signed_csr_client_cert_request_type_dict = update_kms_signed_csr_client_cert_request_type_instance.to_dict()
# create an instance of UpdateKmsSignedCsrClientCertRequestType from a dict
update_kms_signed_csr_client_cert_request_type_form_dict = update_kms_signed_csr_client_cert_request_type.from_dict(update_kms_signed_csr_client_cert_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


