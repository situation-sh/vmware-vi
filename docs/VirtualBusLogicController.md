# VirtualBusLogicController

VirtualBusLogicController is the data object that represents a BusLogic SCSI controller. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_bus_logic_controller import VirtualBusLogicController

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualBusLogicController from a JSON string
virtual_bus_logic_controller_instance = VirtualBusLogicController.from_json(json)
# print the JSON string representation of the object
print VirtualBusLogicController.to_json()

# convert the object into a dict
virtual_bus_logic_controller_dict = virtual_bus_logic_controller_instance.to_dict()
# create an instance of VirtualBusLogicController from a dict
virtual_bus_logic_controller_form_dict = virtual_bus_logic_controller.from_dict(virtual_bus_logic_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


