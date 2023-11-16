# GetCryptoKeyStatusRequestType

The parameters of *CryptoManagerHost.GetCryptoKeyStatus*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[CryptoKeyId]**](CryptoKeyId.md) | \\[in\\] Cryptographic keys to query status.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.get_crypto_key_status_request_type import GetCryptoKeyStatusRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of GetCryptoKeyStatusRequestType from a JSON string
get_crypto_key_status_request_type_instance = GetCryptoKeyStatusRequestType.from_json(json)
# print the JSON string representation of the object
print GetCryptoKeyStatusRequestType.to_json()

# convert the object into a dict
get_crypto_key_status_request_type_dict = get_crypto_key_status_request_type_instance.to_dict()
# create an instance of GetCryptoKeyStatusRequestType from a dict
get_crypto_key_status_request_type_form_dict = get_crypto_key_status_request_type.from_dict(get_crypto_key_status_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


