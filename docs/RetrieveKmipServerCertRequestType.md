# RetrieveKmipServerCertRequestType

The parameters of *CryptoManagerKmip.RetrieveKmipServerCert*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_provider** | [**KeyProviderId**](KeyProviderId.md) |  | 
**server** | [**KmipServerInfo**](KmipServerInfo.md) |  | 

## Example

```python
from vmware_vi.models.retrieve_kmip_server_cert_request_type import RetrieveKmipServerCertRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveKmipServerCertRequestType from a JSON string
retrieve_kmip_server_cert_request_type_instance = RetrieveKmipServerCertRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveKmipServerCertRequestType.to_json()

# convert the object into a dict
retrieve_kmip_server_cert_request_type_dict = retrieve_kmip_server_cert_request_type_instance.to_dict()
# create an instance of RetrieveKmipServerCertRequestType from a dict
retrieve_kmip_server_cert_request_type_form_dict = retrieve_kmip_server_cert_request_type.from_dict(retrieve_kmip_server_cert_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


