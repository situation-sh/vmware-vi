# SetKeyCustomAttributesRequestType

The parameters of *CryptoManagerKmip.SetKeyCustomAttributes*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | 
**spec** | [**CryptoManagerKmipCustomAttributeSpec**](CryptoManagerKmipCustomAttributeSpec.md) |  | 

## Example

```python
from vmware_vi.models.set_key_custom_attributes_request_type import SetKeyCustomAttributesRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetKeyCustomAttributesRequestType from a JSON string
set_key_custom_attributes_request_type_instance = SetKeyCustomAttributesRequestType.from_json(json)
# print the JSON string representation of the object
print SetKeyCustomAttributesRequestType.to_json()

# convert the object into a dict
set_key_custom_attributes_request_type_dict = set_key_custom_attributes_request_type_instance.to_dict()
# create an instance of SetKeyCustomAttributesRequestType from a dict
set_key_custom_attributes_request_type_form_dict = set_key_custom_attributes_request_type.from_dict(set_key_custom_attributes_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


