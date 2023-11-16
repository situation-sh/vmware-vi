# CustomizationIdentitySettings

Base type for sysprep, sysprepText, or linuxPrep object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_identity_settings import CustomizationIdentitySettings

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationIdentitySettings from a JSON string
customization_identity_settings_instance = CustomizationIdentitySettings.from_json(json)
# print the JSON string representation of the object
print CustomizationIdentitySettings.to_json()

# convert the object into a dict
customization_identity_settings_dict = customization_identity_settings_instance.to_dict()
# create an instance of CustomizationIdentitySettings from a dict
customization_identity_settings_form_dict = customization_identity_settings.from_dict(customization_identity_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


