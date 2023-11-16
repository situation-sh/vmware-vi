# VirtualBusLogicControllerOption

This data object contains the options for a BusLogic SCSI controller. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_bus_logic_controller_option import VirtualBusLogicControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualBusLogicControllerOption from a JSON string
virtual_bus_logic_controller_option_instance = VirtualBusLogicControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualBusLogicControllerOption.to_json()

# convert the object into a dict
virtual_bus_logic_controller_option_dict = virtual_bus_logic_controller_option_instance.to_dict()
# create an instance of VirtualBusLogicControllerOption from a dict
virtual_bus_logic_controller_option_form_dict = virtual_bus_logic_controller_option.from_dict(virtual_bus_logic_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


