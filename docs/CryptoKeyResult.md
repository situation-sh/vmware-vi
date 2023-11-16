# CryptoKeyResult

CryptoKeyResult.java -- Data Object representing a cryptographic key operation result.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | 
**success** | **bool** |  | 
**reason** | **str** |  | [optional] 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.crypto_key_result import CryptoKeyResult

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoKeyResult from a JSON string
crypto_key_result_instance = CryptoKeyResult.from_json(json)
# print the JSON string representation of the object
print CryptoKeyResult.to_json()

# convert the object into a dict
crypto_key_result_dict = crypto_key_result_instance.to_dict()
# create an instance of CryptoKeyResult from a dict
crypto_key_result_form_dict = crypto_key_result.from_dict(crypto_key_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


