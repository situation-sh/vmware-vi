# RetrieveClientCertRequestType

The parameters of *CryptoManagerKmip.RetrieveClientCert*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**KeyProviderId**](KeyProviderId.md) |  | 

## Example

```python
from vmware_vi.models.retrieve_client_cert_request_type import RetrieveClientCertRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveClientCertRequestType from a JSON string
retrieve_client_cert_request_type_instance = RetrieveClientCertRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveClientCertRequestType.to_json()

# convert the object into a dict
retrieve_client_cert_request_type_dict = retrieve_client_cert_request_type_instance.to_dict()
# create an instance of RetrieveClientCertRequestType from a dict
retrieve_client_cert_request_type_form_dict = retrieve_client_cert_request_type.from_dict(retrieve_client_cert_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


