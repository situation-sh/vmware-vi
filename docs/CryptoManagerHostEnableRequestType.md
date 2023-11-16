# CryptoManagerHostEnableRequestType

The parameters of *CryptoManagerHost.CryptoManagerHostEnable*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial_key** | [**CryptoKeyPlain**](CryptoKeyPlain.md) |  | 

## Example

```python
from vmware_vi.models.crypto_manager_host_enable_request_type import CryptoManagerHostEnableRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoManagerHostEnableRequestType from a JSON string
crypto_manager_host_enable_request_type_instance = CryptoManagerHostEnableRequestType.from_json(json)
# print the JSON string representation of the object
print CryptoManagerHostEnableRequestType.to_json()

# convert the object into a dict
crypto_manager_host_enable_request_type_dict = crypto_manager_host_enable_request_type_instance.to_dict()
# create an instance of CryptoManagerHostEnableRequestType from a dict
crypto_manager_host_enable_request_type_form_dict = crypto_manager_host_enable_request_type.from_dict(crypto_manager_host_enable_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


