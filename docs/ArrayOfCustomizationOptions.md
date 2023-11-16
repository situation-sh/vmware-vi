# ArrayOfCustomizationOptions

A boxed array of *CustomizationOptions*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationOptions]**](CustomizationOptions.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_options import ArrayOfCustomizationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationOptions from a JSON string
array_of_customization_options_instance = ArrayOfCustomizationOptions.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationOptions.to_json()

# convert the object into a dict
array_of_customization_options_dict = array_of_customization_options_instance.to_dict()
# create an instance of ArrayOfCustomizationOptions from a dict
array_of_customization_options_form_dict = array_of_customization_options.from_dict(array_of_customization_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


