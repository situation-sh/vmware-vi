# ArrayOfKeyValue

A boxed array of *KeyValue*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[KeyValue]**](KeyValue.md) |  | 

## Example

```python
from vmware_vi.models.array_of_key_value import ArrayOfKeyValue

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfKeyValue from a JSON string
array_of_key_value_instance = ArrayOfKeyValue.from_json(json)
# print the JSON string representation of the object
print ArrayOfKeyValue.to_json()

# convert the object into a dict
array_of_key_value_dict = array_of_key_value_instance.to_dict()
# create an instance of ArrayOfKeyValue from a dict
array_of_key_value_form_dict = array_of_key_value.from_dict(array_of_key_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


