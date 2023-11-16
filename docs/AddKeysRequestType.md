# AddKeysRequestType

The parameters of *CryptoManager.AddKeys*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[CryptoKeyPlain]**](CryptoKeyPlain.md) | \\[in\\] List of cryptographic keys to add.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.add_keys_request_type import AddKeysRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AddKeysRequestType from a JSON string
add_keys_request_type_instance = AddKeysRequestType.from_json(json)
# print the JSON string representation of the object
print AddKeysRequestType.to_json()

# convert the object into a dict
add_keys_request_type_dict = add_keys_request_type_instance.to_dict()
# create an instance of AddKeysRequestType from a dict
add_keys_request_type_form_dict = add_keys_request_type.from_dict(add_keys_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


