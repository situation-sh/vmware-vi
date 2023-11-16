# ArrayOfOptionValue

A boxed array of *OptionValue*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OptionValue]**](OptionValue.md) |  | 

## Example

```python
from vmware_vi.models.array_of_option_value import ArrayOfOptionValue

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOptionValue from a JSON string
array_of_option_value_instance = ArrayOfOptionValue.from_json(json)
# print the JSON string representation of the object
print ArrayOfOptionValue.to_json()

# convert the object into a dict
array_of_option_value_dict = array_of_option_value_instance.to_dict()
# create an instance of ArrayOfOptionValue from a dict
array_of_option_value_form_dict = array_of_option_value.from_dict(array_of_option_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


