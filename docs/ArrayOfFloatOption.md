# ArrayOfFloatOption

A boxed array of *FloatOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[FloatOption]**](FloatOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_float_option import ArrayOfFloatOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfFloatOption from a JSON string
array_of_float_option_instance = ArrayOfFloatOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfFloatOption.to_json()

# convert the object into a dict
array_of_float_option_dict = array_of_float_option_instance.to_dict()
# create an instance of ArrayOfFloatOption from a dict
array_of_float_option_form_dict = array_of_float_option.from_dict(array_of_float_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


