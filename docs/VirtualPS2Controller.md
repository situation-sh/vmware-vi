# VirtualPS2Controller

The VirtualPS2Controller data object type represents a controller for keyboards and mice. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_ps2_controller import VirtualPS2Controller

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPS2Controller from a JSON string
virtual_ps2_controller_instance = VirtualPS2Controller.from_json(json)
# print the JSON string representation of the object
print VirtualPS2Controller.to_json()

# convert the object into a dict
virtual_ps2_controller_dict = virtual_ps2_controller_instance.to_dict()
# create an instance of VirtualPS2Controller from a dict
virtual_ps2_controller_form_dict = virtual_ps2_controller.from_dict(virtual_ps2_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


