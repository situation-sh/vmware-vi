# OptionType

The base data object type for all options. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_is_readonly** | **bool** | The flag to indicate whether or not a user can modify a value belonging to this option type.  If the flag is not set, the value can be modified.  | [optional] 

## Example

```python
from vmware_vi.models.option_type import OptionType

# TODO update the JSON string below
json = "{}"
# create an instance of OptionType from a JSON string
option_type_instance = OptionType.from_json(json)
# print the JSON string representation of the object
print OptionType.to_json()

# convert the object into a dict
option_type_dict = option_type_instance.to_dict()
# create an instance of OptionType from a dict
option_type_form_dict = option_type.from_dict(option_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


