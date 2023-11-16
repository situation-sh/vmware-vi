# BoolOption

The BoolOption data object type describes if an option is supported (\"true\") and if the option is set to \"true\" or \"false\" by default. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported** | **bool** | The flag to indicate whether or not the option is supported.  | 
**default_value** | **bool** | The default value for the option.  | 

## Example

```python
from vmware_vi.models.bool_option import BoolOption

# TODO update the JSON string below
json = "{}"
# create an instance of BoolOption from a JSON string
bool_option_instance = BoolOption.from_json(json)
# print the JSON string representation of the object
print BoolOption.to_json()

# convert the object into a dict
bool_option_dict = bool_option_instance.to_dict()
# create an instance of BoolOption from a dict
bool_option_form_dict = bool_option.from_dict(bool_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


