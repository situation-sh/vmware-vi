# ArrayOfCryptoKeyResult

A boxed array of *CryptoKeyResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CryptoKeyResult]**](CryptoKeyResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_crypto_key_result import ArrayOfCryptoKeyResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCryptoKeyResult from a JSON string
array_of_crypto_key_result_instance = ArrayOfCryptoKeyResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfCryptoKeyResult.to_json()

# convert the object into a dict
array_of_crypto_key_result_dict = array_of_crypto_key_result_instance.to_dict()
# create an instance of ArrayOfCryptoKeyResult from a dict
array_of_crypto_key_result_form_dict = array_of_crypto_key_result.from_dict(array_of_crypto_key_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


