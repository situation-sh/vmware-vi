# ArrayOfCryptoKeyPlain

A boxed array of *CryptoKeyPlain*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CryptoKeyPlain]**](CryptoKeyPlain.md) |  | 

## Example

```python
from vmware_vi.models.array_of_crypto_key_plain import ArrayOfCryptoKeyPlain

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCryptoKeyPlain from a JSON string
array_of_crypto_key_plain_instance = ArrayOfCryptoKeyPlain.from_json(json)
# print the JSON string representation of the object
print ArrayOfCryptoKeyPlain.to_json()

# convert the object into a dict
array_of_crypto_key_plain_dict = array_of_crypto_key_plain_instance.to_dict()
# create an instance of ArrayOfCryptoKeyPlain from a dict
array_of_crypto_key_plain_form_dict = array_of_crypto_key_plain.from_dict(array_of_crypto_key_plain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


