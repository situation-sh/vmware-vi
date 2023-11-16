# ArrayOfCustomizationWinOptions

A boxed array of *CustomizationWinOptions*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationWinOptions]**](CustomizationWinOptions.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_win_options import ArrayOfCustomizationWinOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationWinOptions from a JSON string
array_of_customization_win_options_instance = ArrayOfCustomizationWinOptions.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationWinOptions.to_json()

# convert the object into a dict
array_of_customization_win_options_dict = array_of_customization_win_options_instance.to_dict()
# create an instance of ArrayOfCustomizationWinOptions from a dict
array_of_customization_win_options_form_dict = array_of_customization_win_options.from_dict(array_of_customization_win_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


