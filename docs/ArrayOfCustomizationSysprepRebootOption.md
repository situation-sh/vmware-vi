# ArrayOfCustomizationSysprepRebootOption

A boxed array of *CustomizationSysprepRebootOption_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationSysprepRebootOptionEnum]**](CustomizationSysprepRebootOptionEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_sysprep_reboot_option import ArrayOfCustomizationSysprepRebootOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationSysprepRebootOption from a JSON string
array_of_customization_sysprep_reboot_option_instance = ArrayOfCustomizationSysprepRebootOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationSysprepRebootOption.to_json()

# convert the object into a dict
array_of_customization_sysprep_reboot_option_dict = array_of_customization_sysprep_reboot_option_instance.to_dict()
# create an instance of ArrayOfCustomizationSysprepRebootOption from a dict
array_of_customization_sysprep_reboot_option_form_dict = array_of_customization_sysprep_reboot_option.from_dict(array_of_customization_sysprep_reboot_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


