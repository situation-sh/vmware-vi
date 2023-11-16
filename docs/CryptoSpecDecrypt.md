# CryptoSpecDecrypt

This data object type encapsulates virtual machine or disk encryption settings for decryption operation.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.crypto_spec_decrypt import CryptoSpecDecrypt

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoSpecDecrypt from a JSON string
crypto_spec_decrypt_instance = CryptoSpecDecrypt.from_json(json)
# print the JSON string representation of the object
print CryptoSpecDecrypt.to_json()

# convert the object into a dict
crypto_spec_decrypt_dict = crypto_spec_decrypt_instance.to_dict()
# create an instance of CryptoSpecDecrypt from a dict
crypto_spec_decrypt_form_dict = crypto_spec_decrypt.from_dict(crypto_spec_decrypt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


