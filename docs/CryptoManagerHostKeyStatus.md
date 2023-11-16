# CryptoManagerHostKeyStatus

Status of a Crypto key on host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | 
**present** | **bool** | Whether the key is present in key cache for crypto operation.  | 
**management_type** | **str** | Key management type.  See *CryptoManagerHostKeyManagementType_enum* for valid values.  | [optional] 

## Example

```python
from vmware_vi.models.crypto_manager_host_key_status import CryptoManagerHostKeyStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoManagerHostKeyStatus from a JSON string
crypto_manager_host_key_status_instance = CryptoManagerHostKeyStatus.from_json(json)
# print the JSON string representation of the object
print CryptoManagerHostKeyStatus.to_json()

# convert the object into a dict
crypto_manager_host_key_status_dict = crypto_manager_host_key_status_instance.to_dict()
# create an instance of CryptoManagerHostKeyStatus from a dict
crypto_manager_host_key_status_form_dict = crypto_manager_host_key_status.from_dict(crypto_manager_host_key_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


