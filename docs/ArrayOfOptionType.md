# ArrayOfOptionType

A boxed array of *OptionType*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OptionType]**](OptionType.md) |  | 

## Example

```python
from vmware_vi.models.array_of_option_type import ArrayOfOptionType

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOptionType from a JSON string
array_of_option_type_instance = ArrayOfOptionType.from_json(json)
# print the JSON string representation of the object
print ArrayOfOptionType.to_json()

# convert the object into a dict
array_of_option_type_dict = array_of_option_type_instance.to_dict()
# create an instance of ArrayOfOptionType from a dict
array_of_option_type_form_dict = array_of_option_type.from_dict(array_of_option_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


