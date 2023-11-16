# UpdateSelfSignedClientCertRequestType

The parameters of *CryptoManagerKmip.UpdateSelfSignedClientCert*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**KeyProviderId**](KeyProviderId.md) |  | 
**certificate** | **str** | \\[in\\] Client certificate.  | 

## Example

```python
from vmware_vi.models.update_self_signed_client_cert_request_type import UpdateSelfSignedClientCertRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSelfSignedClientCertRequestType from a JSON string
update_self_signed_client_cert_request_type_instance = UpdateSelfSignedClientCertRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateSelfSignedClientCertRequestType.to_json()

# convert the object into a dict
update_self_signed_client_cert_request_type_dict = update_self_signed_client_cert_request_type_instance.to_dict()
# create an instance of UpdateSelfSignedClientCertRequestType from a dict
update_self_signed_client_cert_request_type_form_dict = update_self_signed_client_cert_request_type.from_dict(update_self_signed_client_cert_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


