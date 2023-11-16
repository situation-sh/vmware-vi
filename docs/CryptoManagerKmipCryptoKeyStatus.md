# CryptoManagerKmipCryptoKeyStatus

Status of a Crypto key  ***Since:*** vSphere API 6.7.2 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | 
**key_available** | **bool** | If the key is available for crypto operation  ***Since:*** vSphere API 6.7.2  | [optional] 
**reason** | **str** | The reason for key not available, valid when keyAvailable is false.  *CryptoManagerKmipCryptoKeyStatusKeyUnavailableReason_enum* lists the set of supported values.  ***Since:*** vSphere API 6.7.2  | [optional] 
**encrypted_vms** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The list of VMs which use that key  ***Since:*** vSphere API 6.7.2  Refers instances of *VirtualMachine*.  | [optional] 
**affected_hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The lists of hosts which use that key as host key  ***Since:*** vSphere API 6.7.2  Refers instances of *HostSystem*.  | [optional] 
**referenced_by_tags** | **List[str]** | The identifier list for the 3rd party who are using the key  ***Since:*** vSphere API 6.7.2  | [optional] 

## Example

```python
from vmware_vi.models.crypto_manager_kmip_crypto_key_status import CryptoManagerKmipCryptoKeyStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoManagerKmipCryptoKeyStatus from a JSON string
crypto_manager_kmip_crypto_key_status_instance = CryptoManagerKmipCryptoKeyStatus.from_json(json)
# print the JSON string representation of the object
print CryptoManagerKmipCryptoKeyStatus.to_json()

# convert the object into a dict
crypto_manager_kmip_crypto_key_status_dict = crypto_manager_kmip_crypto_key_status_instance.to_dict()
# create an instance of CryptoManagerKmipCryptoKeyStatus from a dict
crypto_manager_kmip_crypto_key_status_form_dict = crypto_manager_kmip_crypto_key_status.from_dict(crypto_manager_kmip_crypto_key_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


