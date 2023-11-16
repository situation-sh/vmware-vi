# GenerateClientCsrRequestType

The parameters of *CryptoManagerKmip.GenerateClientCsr*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**KeyProviderId**](KeyProviderId.md) |  | 
**request** | [**CryptoManagerKmipCertSignRequest**](CryptoManagerKmipCertSignRequest.md) |  | [optional] 

## Example

```python
from vmware_vi.models.generate_client_csr_request_type import GenerateClientCsrRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateClientCsrRequestType from a JSON string
generate_client_csr_request_type_instance = GenerateClientCsrRequestType.from_json(json)
# print the JSON string representation of the object
print GenerateClientCsrRequestType.to_json()

# convert the object into a dict
generate_client_csr_request_type_dict = generate_client_csr_request_type_instance.to_dict()
# create an instance of GenerateClientCsrRequestType from a dict
generate_client_csr_request_type_form_dict = generate_client_csr_request_type.from_dict(generate_client_csr_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


