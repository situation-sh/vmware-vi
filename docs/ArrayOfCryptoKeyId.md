# ArrayOfCryptoKeyId

A boxed array of *CryptoKeyId*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CryptoKeyId]**](CryptoKeyId.md) |  | 

## Example

```python
from vmware_vi.models.array_of_crypto_key_id import ArrayOfCryptoKeyId

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCryptoKeyId from a JSON string
array_of_crypto_key_id_instance = ArrayOfCryptoKeyId.from_json(json)
# print the JSON string representation of the object
print ArrayOfCryptoKeyId.to_json()

# convert the object into a dict
array_of_crypto_key_id_dict = array_of_crypto_key_id_instance.to_dict()
# create an instance of ArrayOfCryptoKeyId from a dict
array_of_crypto_key_id_form_dict = array_of_crypto_key_id.from_dict(array_of_crypto_key_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


