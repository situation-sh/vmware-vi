# UploadClientCertRequestType

The parameters of *CryptoManagerKmip.UploadClientCert*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**KeyProviderId**](KeyProviderId.md) |  | 
**certificate** | **str** | \\[in\\] Client certificate.  | 
**private_key** | **str** | \\[in\\] Private key.  | 

## Example

```python
from vmware_vi.models.upload_client_cert_request_type import UploadClientCertRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UploadClientCertRequestType from a JSON string
upload_client_cert_request_type_instance = UploadClientCertRequestType.from_json(json)
# print the JSON string representation of the object
print UploadClientCertRequestType.to_json()

# convert the object into a dict
upload_client_cert_request_type_dict = upload_client_cert_request_type_instance.to_dict()
# create an instance of UploadClientCertRequestType from a dict
upload_client_cert_request_type_form_dict = upload_client_cert_request_type.from_dict(upload_client_cert_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


