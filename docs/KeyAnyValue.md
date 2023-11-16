# KeyAnyValue

Non-localized key/value pair in which the the value can be of any type.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | the key  ***Since:*** vSphere API 4.0  | 
**value** | [**Any**](Any.md) |  | 

## Example

```python
from vmware_vi.models.key_any_value import KeyAnyValue

# TODO update the JSON string below
json = "{}"
# create an instance of KeyAnyValue from a JSON string
key_any_value_instance = KeyAnyValue.from_json(json)
# print the JSON string representation of the object
print KeyAnyValue.to_json()

# convert the object into a dict
key_any_value_dict = key_any_value_instance.to_dict()
# create an instance of KeyAnyValue from a dict
key_any_value_form_dict = key_any_value.from_dict(key_any_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


