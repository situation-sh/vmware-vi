# CryptoSpec

This data object type encapsulates virtual machine or disk encryption settings.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.crypto_spec import CryptoSpec

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoSpec from a JSON string
crypto_spec_instance = CryptoSpec.from_json(json)
# print the JSON string representation of the object
print CryptoSpec.to_json()

# convert the object into a dict
crypto_spec_dict = crypto_spec_instance.to_dict()
# create an instance of CryptoSpec from a dict
crypto_spec_form_dict = crypto_spec.from_dict(crypto_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


