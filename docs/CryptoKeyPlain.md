# CryptoKeyPlain

Data Object representing a plain text cryptographic key.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | 
**algorithm** | **str** |  | 
**key_data** | **str** |  | 

## Example

```python
from vmware_vi.models.crypto_key_plain import CryptoKeyPlain

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoKeyPlain from a JSON string
crypto_key_plain_instance = CryptoKeyPlain.from_json(json)
# print the JSON string representation of the object
print CryptoKeyPlain.to_json()

# convert the object into a dict
crypto_key_plain_dict = crypto_key_plain_instance.to_dict()
# create an instance of CryptoKeyPlain from a dict
crypto_key_plain_form_dict = crypto_key_plain.from_dict(crypto_key_plain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


