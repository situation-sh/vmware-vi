# RemoveKeysRequestType

The parameters of *CryptoManager.RemoveKeys*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[CryptoKeyId]**](CryptoKeyId.md) | \\[in\\] List of keys to remove.  ***Since:*** vSphere API 6.5  | [optional] 
**force** | **bool** | \\[in\\] Remove the key even if in use. Always successful.  | 

## Example

```python
from vmware_vi.models.remove_keys_request_type import RemoveKeysRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveKeysRequestType from a JSON string
remove_keys_request_type_instance = RemoveKeysRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveKeysRequestType.to_json()

# convert the object into a dict
remove_keys_request_type_dict = remove_keys_request_type_instance.to_dict()
# create an instance of RemoveKeysRequestType from a dict
remove_keys_request_type_form_dict = remove_keys_request_type.from_dict(remove_keys_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


