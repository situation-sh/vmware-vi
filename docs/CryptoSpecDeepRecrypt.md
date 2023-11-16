# CryptoSpecDeepRecrypt

This data object type encapsulates virtual machine or disk cryptographic settings for deep reencryption operation.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | 

## Example

```python
from vmware_vi.models.crypto_spec_deep_recrypt import CryptoSpecDeepRecrypt

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoSpecDeepRecrypt from a JSON string
crypto_spec_deep_recrypt_instance = CryptoSpecDeepRecrypt.from_json(json)
# print the JSON string representation of the object
print CryptoSpecDeepRecrypt.to_json()

# convert the object into a dict
crypto_spec_deep_recrypt_dict = crypto_spec_deep_recrypt_instance.to_dict()
# create an instance of CryptoSpecDeepRecrypt from a dict
crypto_spec_deep_recrypt_form_dict = crypto_spec_deep_recrypt.from_dict(crypto_spec_deep_recrypt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


