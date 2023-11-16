# AddKeyRequestType

The parameters of *CryptoManager.AddKey*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**CryptoKeyPlain**](CryptoKeyPlain.md) |  | 

## Example

```python
from vmware_vi.models.add_key_request_type import AddKeyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddKeyRequestType from a JSON string
add_key_request_type_instance = AddKeyRequestType.from_json(json)
# print the JSON string representation of the object
print AddKeyRequestType.to_json()

# convert the object into a dict
add_key_request_type_dict = add_key_request_type_instance.to_dict()
# create an instance of AddKeyRequestType from a dict
add_key_request_type_form_dict = add_key_request_type.from_dict(add_key_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


