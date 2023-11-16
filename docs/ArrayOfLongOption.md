# ArrayOfLongOption

A boxed array of *LongOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LongOption]**](LongOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_long_option import ArrayOfLongOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLongOption from a JSON string
array_of_long_option_instance = ArrayOfLongOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfLongOption.to_json()

# convert the object into a dict
array_of_long_option_dict = array_of_long_option_instance.to_dict()
# create an instance of ArrayOfLongOption from a dict
array_of_long_option_form_dict = array_of_long_option.from_dict(array_of_long_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


