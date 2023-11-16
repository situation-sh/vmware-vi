# ArrayOfCryptoSpec

A boxed array of *CryptoSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CryptoSpec]**](CryptoSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_crypto_spec import ArrayOfCryptoSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCryptoSpec from a JSON string
array_of_crypto_spec_instance = ArrayOfCryptoSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfCryptoSpec.to_json()

# convert the object into a dict
array_of_crypto_spec_dict = array_of_crypto_spec_instance.to_dict()
# create an instance of ArrayOfCryptoSpec from a dict
array_of_crypto_spec_form_dict = array_of_crypto_spec.from_dict(array_of_crypto_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


