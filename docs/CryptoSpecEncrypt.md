# CryptoSpecEncrypt

This data object type encapsulates virtual machine or disk cryptohraphic settings for encryption operation.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | 

## Example

```python
from vmware_vi.models.crypto_spec_encrypt import CryptoSpecEncrypt

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoSpecEncrypt from a JSON string
crypto_spec_encrypt_instance = CryptoSpecEncrypt.from_json(json)
# print the JSON string representation of the object
print CryptoSpecEncrypt.to_json()

# convert the object into a dict
crypto_spec_encrypt_dict = crypto_spec_encrypt_instance.to_dict()
# create an instance of CryptoSpecEncrypt from a dict
crypto_spec_encrypt_form_dict = crypto_spec_encrypt.from_dict(crypto_spec_encrypt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


