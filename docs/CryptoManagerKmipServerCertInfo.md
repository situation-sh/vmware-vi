# CryptoManagerKmipServerCertInfo

Information about the KMIP server certificate.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | The server certificate.  ***Since:*** vSphere API 6.5  | 
**cert_info** | [**CryptoManagerKmipCertificateInfo**](CryptoManagerKmipCertificateInfo.md) |  | [optional] 
**client_trust_server** | **bool** | Whether this KMS server is trusted by local Kmip client.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.crypto_manager_kmip_server_cert_info import CryptoManagerKmipServerCertInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoManagerKmipServerCertInfo from a JSON string
crypto_manager_kmip_server_cert_info_instance = CryptoManagerKmipServerCertInfo.from_json(json)
# print the JSON string representation of the object
print CryptoManagerKmipServerCertInfo.to_json()

# convert the object into a dict
crypto_manager_kmip_server_cert_info_dict = crypto_manager_kmip_server_cert_info_instance.to_dict()
# create an instance of CryptoManagerKmipServerCertInfo from a dict
crypto_manager_kmip_server_cert_info_form_dict = crypto_manager_kmip_server_cert_info.from_dict(crypto_manager_kmip_server_cert_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


