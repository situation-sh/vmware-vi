# CryptoManagerKmipServerStatus

Status of a KMIP server.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the KMIP server.  ***Since:*** vSphere API 6.5  | 
**status** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | 
**connection_status** | **str** | KMIP server connection status description.  ***Since:*** vSphere API 6.5  | 
**cert_info** | [**CryptoManagerKmipCertificateInfo**](CryptoManagerKmipCertificateInfo.md) |  | [optional] 
**client_trust_server** | **bool** | Whether this KMS server is trusted by local Kmip client.  ***Since:*** vSphere API 6.5  | [optional] 
**server_trust_client** | **bool** | Whether this KMS server trusts the local Kmip client.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.crypto_manager_kmip_server_status import CryptoManagerKmipServerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoManagerKmipServerStatus from a JSON string
crypto_manager_kmip_server_status_instance = CryptoManagerKmipServerStatus.from_json(json)
# print the JSON string representation of the object
print CryptoManagerKmipServerStatus.to_json()

# convert the object into a dict
crypto_manager_kmip_server_status_dict = crypto_manager_kmip_server_status_instance.to_dict()
# create an instance of CryptoManagerKmipServerStatus from a dict
crypto_manager_kmip_server_status_form_dict = crypto_manager_kmip_server_status.from_dict(crypto_manager_kmip_server_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


