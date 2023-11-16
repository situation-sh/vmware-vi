# StringOption

The StringOption data object type is used to define an open-ended string value based on an optional subset of valid characters. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_value** | **str** | The default value.  | 
**valid_characters** | **str** | The string containing the set of valid characters.  If a string option is not specified, all strings are allowed.  | [optional] 

## Example

```python
from vmware_vi.models.string_option import StringOption

# TODO update the JSON string below
json = "{}"
# create an instance of StringOption from a JSON string
string_option_instance = StringOption.from_json(json)
# print the JSON string representation of the object
print StringOption.to_json()

# convert the object into a dict
string_option_dict = string_option_instance.to_dict()
# create an instance of StringOption from a dict
string_option_form_dict = string_option.from_dict(string_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


