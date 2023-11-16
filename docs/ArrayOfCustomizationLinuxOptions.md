# ArrayOfCustomizationLinuxOptions

A boxed array of *CustomizationLinuxOptions*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationLinuxOptions]**](CustomizationLinuxOptions.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_linux_options import ArrayOfCustomizationLinuxOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationLinuxOptions from a JSON string
array_of_customization_linux_options_instance = ArrayOfCustomizationLinuxOptions.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationLinuxOptions.to_json()

# convert the object into a dict
array_of_customization_linux_options_dict = array_of_customization_linux_options_instance.to_dict()
# create an instance of ArrayOfCustomizationLinuxOptions from a dict
array_of_customization_linux_options_form_dict = array_of_customization_linux_options.from_dict(array_of_customization_linux_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


