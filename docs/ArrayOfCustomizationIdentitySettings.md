# ArrayOfCustomizationIdentitySettings

A boxed array of *CustomizationIdentitySettings*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationIdentitySettings]**](CustomizationIdentitySettings.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_identity_settings import ArrayOfCustomizationIdentitySettings

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationIdentitySettings from a JSON string
array_of_customization_identity_settings_instance = ArrayOfCustomizationIdentitySettings.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationIdentitySettings.to_json()

# convert the object into a dict
array_of_customization_identity_settings_dict = array_of_customization_identity_settings_instance.to_dict()
# create an instance of ArrayOfCustomizationIdentitySettings from a dict
array_of_customization_identity_settings_form_dict = array_of_customization_identity_settings.from_dict(array_of_customization_identity_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


