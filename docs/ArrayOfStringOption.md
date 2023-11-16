# ArrayOfStringOption

A boxed array of *StringOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StringOption]**](StringOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_string_option import ArrayOfStringOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStringOption from a JSON string
array_of_string_option_instance = ArrayOfStringOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfStringOption.to_json()

# convert the object into a dict
array_of_string_option_dict = array_of_string_option_instance.to_dict()
# create an instance of ArrayOfStringOption from a dict
array_of_string_option_form_dict = array_of_string_option.from_dict(array_of_string_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


