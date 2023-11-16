# ConfigureCryptoKeyRequestType

The parameters of *HostSystem.ConfigureCryptoKey*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | [optional] 

## Example

```python
from vmware_vi.models.configure_crypto_key_request_type import ConfigureCryptoKeyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigureCryptoKeyRequestType from a JSON string
configure_crypto_key_request_type_instance = ConfigureCryptoKeyRequestType.from_json(json)
# print the JSON string representation of the object
print ConfigureCryptoKeyRequestType.to_json()

# convert the object into a dict
configure_crypto_key_request_type_dict = configure_crypto_key_request_type_instance.to_dict()
# create an instance of ConfigureCryptoKeyRequestType from a dict
configure_crypto_key_request_type_form_dict = configure_crypto_key_request_type.from_dict(configure_crypto_key_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


