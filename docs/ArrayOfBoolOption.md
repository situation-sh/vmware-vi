# ArrayOfBoolOption

A boxed array of *BoolOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[BoolOption]**](BoolOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_bool_option import ArrayOfBoolOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfBoolOption from a JSON string
array_of_bool_option_instance = ArrayOfBoolOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfBoolOption.to_json()

# convert the object into a dict
array_of_bool_option_dict = array_of_bool_option_instance.to_dict()
# create an instance of ArrayOfBoolOption from a dict
array_of_bool_option_form_dict = array_of_bool_option.from_dict(array_of_bool_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


