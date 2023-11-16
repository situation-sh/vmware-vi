# ArrayOfChoiceOption

A boxed array of *ChoiceOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ChoiceOption]**](ChoiceOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_choice_option import ArrayOfChoiceOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfChoiceOption from a JSON string
array_of_choice_option_instance = ArrayOfChoiceOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfChoiceOption.to_json()

# convert the object into a dict
array_of_choice_option_dict = array_of_choice_option_instance.to_dict()
# create an instance of ArrayOfChoiceOption from a dict
array_of_choice_option_form_dict = array_of_choice_option.from_dict(array_of_choice_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


