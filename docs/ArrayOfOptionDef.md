# ArrayOfOptionDef

A boxed array of *OptionDef*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OptionDef]**](OptionDef.md) |  | 

## Example

```python
from vmware_vi.models.array_of_option_def import ArrayOfOptionDef

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOptionDef from a JSON string
array_of_option_def_instance = ArrayOfOptionDef.from_json(json)
# print the JSON string representation of the object
print ArrayOfOptionDef.to_json()

# convert the object into a dict
array_of_option_def_dict = array_of_option_def_instance.to_dict()
# create an instance of ArrayOfOptionDef from a dict
array_of_option_def_form_dict = array_of_option_def.from_dict(array_of_option_def_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


