# CustomizationSysprepRebootOption

A boxed *CustomizationSysprepRebootOption_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**CustomizationSysprepRebootOptionEnum**](CustomizationSysprepRebootOptionEnum.md) |  | 

## Example

```python
from vmware_vi.models.customization_sysprep_reboot_option import CustomizationSysprepRebootOption

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationSysprepRebootOption from a JSON string
customization_sysprep_reboot_option_instance = CustomizationSysprepRebootOption.from_json(json)
# print the JSON string representation of the object
print CustomizationSysprepRebootOption.to_json()

# convert the object into a dict
customization_sysprep_reboot_option_dict = customization_sysprep_reboot_option_instance.to_dict()
# create an instance of CustomizationSysprepRebootOption from a dict
customization_sysprep_reboot_option_form_dict = customization_sysprep_reboot_option.from_dict(customization_sysprep_reboot_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


