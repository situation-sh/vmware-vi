# ArrayOfIntOption

A boxed array of *IntOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IntOption]**](IntOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_int_option import ArrayOfIntOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIntOption from a JSON string
array_of_int_option_instance = ArrayOfIntOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfIntOption.to_json()

# convert the object into a dict
array_of_int_option_dict = array_of_int_option_instance.to_dict()
# create an instance of ArrayOfIntOption from a dict
array_of_int_option_form_dict = array_of_int_option.from_dict(array_of_int_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


