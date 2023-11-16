# CustomizationLicenseDataMode

A boxed *CustomizationLicenseDataMode_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**CustomizationLicenseDataModeEnum**](CustomizationLicenseDataModeEnum.md) |  | 

## Example

```python
from vmware_vi.models.customization_license_data_mode import CustomizationLicenseDataMode

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationLicenseDataMode from a JSON string
customization_license_data_mode_instance = CustomizationLicenseDataMode.from_json(json)
# print the JSON string representation of the object
print CustomizationLicenseDataMode.to_json()

# convert the object into a dict
customization_license_data_mode_dict = customization_license_data_mode_instance.to_dict()
# create an instance of CustomizationLicenseDataMode from a dict
customization_license_data_mode_form_dict = customization_license_data_mode.from_dict(customization_license_data_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


