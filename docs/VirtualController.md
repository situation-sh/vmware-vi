# VirtualController

VirtualController is the base data object type for a device controller in a virtual machine.  VirtualController extends *VirtualDevice* to inherit general information about a controller (such as name and description), and to allow controllers to appear in a generic list of virtual devices. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bus_number** | **int** | Bus number associated with this controller.  | 
**device** | **List[int]** | List of devices currently controlled by this controller.  Each entry contains the *VirtualDevice.key* property of the corresponding device object.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_controller import VirtualController

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualController from a JSON string
virtual_controller_instance = VirtualController.from_json(json)
# print the JSON string representation of the object
print VirtualController.to_json()

# convert the object into a dict
virtual_controller_dict = virtual_controller_instance.to_dict()
# create an instance of VirtualController from a dict
virtual_controller_form_dict = virtual_controller.from_dict(virtual_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


