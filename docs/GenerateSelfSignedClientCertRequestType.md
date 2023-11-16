# GenerateSelfSignedClientCertRequestType

The parameters of *CryptoManagerKmip.GenerateSelfSignedClientCert*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**KeyProviderId**](KeyProviderId.md) |  | 
**request** | [**CryptoManagerKmipCertSignRequest**](CryptoManagerKmipCertSignRequest.md) |  | [optional] 

## Example

```python
from vmware_vi.models.generate_self_signed_client_cert_request_type import GenerateSelfSignedClientCertRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateSelfSignedClientCertRequestType from a JSON string
generate_self_signed_client_cert_request_type_instance = GenerateSelfSignedClientCertRequestType.from_json(json)
# print the JSON string representation of the object
print GenerateSelfSignedClientCertRequestType.to_json()

# convert the object into a dict
generate_self_signed_client_cert_request_type_dict = generate_self_signed_client_cert_request_type_instance.to_dict()
# create an instance of GenerateSelfSignedClientCertRequestType from a dict
generate_self_signed_client_cert_request_type_form_dict = generate_self_signed_client_cert_request_type.from_dict(generate_self_signed_client_cert_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


