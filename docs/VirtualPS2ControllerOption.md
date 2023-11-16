# VirtualPS2ControllerOption

The VirtualPS2ControllerOption data object type contains the options for a virtual PS/2 controller for keyboards and mice.  In addition to the options defined in the *VirtualControllerOption* data object type, these options include the number of keyboards and mice. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_keyboards** | [**IntOption**](IntOption.md) |  | 
**num_pointing_devices** | [**IntOption**](IntOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_ps2_controller_option import VirtualPS2ControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPS2ControllerOption from a JSON string
virtual_ps2_controller_option_instance = VirtualPS2ControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualPS2ControllerOption.to_json()

# convert the object into a dict
virtual_ps2_controller_option_dict = virtual_ps2_controller_option_instance.to_dict()
# create an instance of VirtualPS2ControllerOption from a dict
virtual_ps2_controller_option_form_dict = virtual_ps2_controller_option.from_dict(virtual_ps2_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


