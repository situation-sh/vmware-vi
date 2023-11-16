# RemoveKeyRequestType

The parameters of *CryptoManager.RemoveKey*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**CryptoKeyId**](CryptoKeyId.md) |  | 
**force** | **bool** | \\[in\\] Remove the key even if in use or not existent.  | 

## Example

```python
from vmware_vi.models.remove_key_request_type import RemoveKeyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveKeyRequestType from a JSON string
remove_key_request_type_instance = RemoveKeyRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveKeyRequestType.to_json()

# convert the object into a dict
remove_key_request_type_dict = remove_key_request_type_instance.to_dict()
# create an instance of RemoveKeyRequestType from a dict
remove_key_request_type_form_dict = remove_key_request_type.from_dict(remove_key_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


