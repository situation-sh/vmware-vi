# CryptoKeyId

Data Object representing a cryptographic key.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | Unique key ID.  When creating a key may be replaced with the ID generated by the KMS server. An empty string must be used when encrypting with a Trusted Key Provider, because the key is generated at the time of encryption.  ***Since:*** vSphere API 6.5  | 
**provider_id** | [**KeyProviderId**](KeyProviderId.md) |  | [optional] 

## Example

```python
from vmware_vi.models.crypto_key_id import CryptoKeyId

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoKeyId from a JSON string
crypto_key_id_instance = CryptoKeyId.from_json(json)
# print the JSON string representation of the object
print CryptoKeyId.to_json()

# convert the object into a dict
crypto_key_id_dict = crypto_key_id_instance.to_dict()
# create an instance of CryptoKeyId from a dict
crypto_key_id_form_dict = crypto_key_id.from_dict(crypto_key_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

