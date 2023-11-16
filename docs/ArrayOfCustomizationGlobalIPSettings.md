# ArrayOfCustomizationGlobalIPSettings

A boxed array of *CustomizationGlobalIPSettings*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationGlobalIPSettings]**](CustomizationGlobalIPSettings.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_global_ip_settings import ArrayOfCustomizationGlobalIPSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationGlobalIPSettings from a JSON string
array_of_customization_global_ip_settings_instance = ArrayOfCustomizationGlobalIPSettings.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationGlobalIPSettings.to_json()

# convert the object into a dict
array_of_customization_global_ip_settings_dict = array_of_customization_global_ip_settings_instance.to_dict()
# create an instance of ArrayOfCustomizationGlobalIPSettings from a dict
array_of_customization_global_ip_settings_form_dict = array_of_customization_global_ip_settings.from_dict(array_of_customization_global_ip_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


