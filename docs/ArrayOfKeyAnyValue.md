# ArrayOfKeyAnyValue

A boxed array of *KeyAnyValue*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[KeyAnyValue]**](KeyAnyValue.md) |  | 

## Example

```python
from vmware_vi.models.array_of_key_any_value import ArrayOfKeyAnyValue

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfKeyAnyValue from a JSON string
array_of_key_any_value_instance = ArrayOfKeyAnyValue.from_json(json)
# print the JSON string representation of the object
print ArrayOfKeyAnyValue.to_json()

# convert the object into a dict
array_of_key_any_value_dict = array_of_key_any_value_instance.to_dict()
# create an instance of ArrayOfKeyAnyValue from a dict
array_of_key_any_value_form_dict = array_of_key_any_value.from_dict(array_of_key_any_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


