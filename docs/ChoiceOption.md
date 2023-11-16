# ChoiceOption

The ChoiceOption data object type defines a set of supported string values, a localizable description for each value, and the default value. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choice_info** | [**List[ElementDescription]**](ElementDescription.md) | The set of possible selections and descriptions.  | 
**default_index** | **int** | The index in ChoiceOption.value that serves as the default value.  | [optional] 

## Example

```python
from vmware_vi.models.choice_option import ChoiceOption

# TODO update the JSON string below
json = "{}"
# create an instance of ChoiceOption from a JSON string
choice_option_instance = ChoiceOption.from_json(json)
# print the JSON string representation of the object
print ChoiceOption.to_json()

# convert the object into a dict
choice_option_dict = choice_option_instance.to_dict()
# create an instance of ChoiceOption from a dict
choice_option_form_dict = choice_option.from_dict(choice_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


