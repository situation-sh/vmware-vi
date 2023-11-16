# CryptoManagerKmipClusterStatus

Status of a KMIP cluster.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | [**KeyProviderId**](KeyProviderId.md) |  | 
**overall_status** | [**ManagedEntityStatusEnum**](ManagedEntityStatusEnum.md) |  | [optional] 
**management_type** | **str** | Key provider management type.  See *KmipClusterInfoKmsManagementType_enum* for valid values.  ***Since:*** vSphere API 7.0  | [optional] 
**servers** | [**List[CryptoManagerKmipServerStatus]**](CryptoManagerKmipServerStatus.md) | Status of the KMIP servers in this cluster.  ***Since:*** vSphere API 6.5  | 
**client_cert_info** | [**CryptoManagerKmipCertificateInfo**](CryptoManagerKmipCertificateInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.crypto_manager_kmip_cluster_status import CryptoManagerKmipClusterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoManagerKmipClusterStatus from a JSON string
crypto_manager_kmip_cluster_status_instance = CryptoManagerKmipClusterStatus.from_json(json)
# print the JSON string representation of the object
print CryptoManagerKmipClusterStatus.to_json()

# convert the object into a dict
crypto_manager_kmip_cluster_status_dict = crypto_manager_kmip_cluster_status_instance.to_dict()
# create an instance of CryptoManagerKmipClusterStatus from a dict
crypto_manager_kmip_cluster_status_form_dict = crypto_manager_kmip_cluster_status.from_dict(crypto_manager_kmip_cluster_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


