# CryptoManagerKmipCustomAttributeSpec

Crypto key custom attribute spec 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[KeyValue]**](KeyValue.md) | Crypto key custom attributes  | [optional] 

## Example

```python
from vmware_vi.models.crypto_manager_kmip_custom_attribute_spec import CryptoManagerKmipCustomAttributeSpec

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoManagerKmipCustomAttributeSpec from a JSON string
crypto_manager_kmip_custom_attribute_spec_instance = CryptoManagerKmipCustomAttributeSpec.from_json(json)
# print the JSON string representation of the object
print CryptoManagerKmipCustomAttributeSpec.to_json()

# convert the object into a dict
crypto_manager_kmip_custom_attribute_spec_dict = crypto_manager_kmip_custom_attribute_spec_instance.to_dict()
# create an instance of CryptoManagerKmipCustomAttributeSpec from a dict
crypto_manager_kmip_custom_attribute_spec_form_dict = crypto_manager_kmip_custom_attribute_spec.from_dict(crypto_manager_kmip_custom_attribute_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


