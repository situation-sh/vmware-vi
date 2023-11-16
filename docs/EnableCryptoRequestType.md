# EnableCryptoRequestType

The parameters of *HostSystem.EnableCrypto*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_plain** | [**CryptoKeyPlain**](CryptoKeyPlain.md) |  | 

## Example

```python
from vmware_vi.models.enable_crypto_request_type import EnableCryptoRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EnableCryptoRequestType from a JSON string
enable_crypto_request_type_instance = EnableCryptoRequestType.from_json(json)
# print the JSON string representation of the object
print EnableCryptoRequestType.to_json()

# convert the object into a dict
enable_crypto_request_type_dict = enable_crypto_request_type_instance.to_dict()
# create an instance of EnableCryptoRequestType from a dict
enable_crypto_request_type_form_dict = enable_crypto_request_type.from_dict(enable_crypto_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


