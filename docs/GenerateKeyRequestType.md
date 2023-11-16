# GenerateKeyRequestType

The parameters of *CryptoManagerKmip.GenerateKey*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_provider** | [**KeyProviderId**](KeyProviderId.md) |  | [optional] 
**spec** | [**CryptoManagerKmipCustomAttributeSpec**](CryptoManagerKmipCustomAttributeSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.generate_key_request_type import GenerateKeyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateKeyRequestType from a JSON string
generate_key_request_type_instance = GenerateKeyRequestType.from_json(json)
# print the JSON string representation of the object
print GenerateKeyRequestType.to_json()

# convert the object into a dict
generate_key_request_type_dict = generate_key_request_type_instance.to_dict()
# create an instance of GenerateKeyRequestType from a dict
generate_key_request_type_form_dict = generate_key_request_type.from_dict(generate_key_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


