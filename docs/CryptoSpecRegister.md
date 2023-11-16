# CryptoSpecRegister

This data object type indicates that the operation requires keys to be sent but the encryption settings of the virtual machine or disk should not be modified by the operation.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | 

## Example

```python
from vmware_vi.models.crypto_spec_register import CryptoSpecRegister

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoSpecRegister from a JSON string
crypto_spec_register_instance = CryptoSpecRegister.from_json(json)
# print the JSON string representation of the object
print CryptoSpecRegister.to_json()

# convert the object into a dict
crypto_spec_register_dict = crypto_spec_register_instance.to_dict()
# create an instance of CryptoSpecRegister from a dict
crypto_spec_register_form_dict = crypto_spec_register.from_dict(crypto_spec_register_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


