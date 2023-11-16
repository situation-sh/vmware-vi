# UploadKmipServerCertRequestType

The parameters of *CryptoManagerKmip.UploadKmipServerCert*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**KeyProviderId**](KeyProviderId.md) |  | 
**certificate** | **str** | \\[in\\] Server certificate in PEM encoding.  | 

## Example

```python
from vmware_vi.models.upload_kmip_server_cert_request_type import UploadKmipServerCertRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UploadKmipServerCertRequestType from a JSON string
upload_kmip_server_cert_request_type_instance = UploadKmipServerCertRequestType.from_json(json)
# print the JSON string representation of the object
print UploadKmipServerCertRequestType.to_json()

# convert the object into a dict
upload_kmip_server_cert_request_type_dict = upload_kmip_server_cert_request_type_instance.to_dict()
# create an instance of UploadKmipServerCertRequestType from a dict
upload_kmip_server_cert_request_type_form_dict = upload_kmip_server_cert_request_type.from_dict(upload_kmip_server_cert_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


