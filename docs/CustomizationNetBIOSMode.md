# CustomizationNetBIOSMode

A boxed *CustomizationNetBIOSMode_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**CustomizationNetBIOSModeEnum**](CustomizationNetBIOSModeEnum.md) |  | 

## Example

```python
from vmware_vi.models.customization_net_bios_mode import CustomizationNetBIOSMode

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationNetBIOSMode from a JSON string
customization_net_bios_mode_instance = CustomizationNetBIOSMode.from_json(json)
# print the JSON string representation of the object
print CustomizationNetBIOSMode.to_json()

# convert the object into a dict
customization_net_bios_mode_dict = customization_net_bios_mode_instance.to_dict()
# create an instance of CustomizationNetBIOSMode from a dict
customization_net_bios_mode_form_dict = customization_net_bios_mode.from_dict(customization_net_bios_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


