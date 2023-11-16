# ArrayOfCustomizationIPSettings

A boxed array of *CustomizationIPSettings*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationIPSettings]**](CustomizationIPSettings.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_ip_settings import ArrayOfCustomizationIPSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationIPSettings from a JSON string
array_of_customization_ip_settings_instance = ArrayOfCustomizationIPSettings.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationIPSettings.to_json()

# convert the object into a dict
array_of_customization_ip_settings_dict = array_of_customization_ip_settings_instance.to_dict()
# create an instance of ArrayOfCustomizationIPSettings from a dict
array_of_customization_ip_settings_form_dict = array_of_customization_ip_settings.from_dict(array_of_customization_ip_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


