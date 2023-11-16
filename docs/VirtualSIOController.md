# VirtualSIOController

This data object type defines a Super IO Controller for floppy drives, parallel ports, and serial ports. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_sio_controller import VirtualSIOController

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSIOController from a JSON string
virtual_sio_controller_instance = VirtualSIOController.from_json(json)
# print the JSON string representation of the object
print VirtualSIOController.to_json()

# convert the object into a dict
virtual_sio_controller_dict = virtual_sio_controller_instance.to_dict()
# create an instance of VirtualSIOController from a dict
virtual_sio_controller_form_dict = virtual_sio_controller.from_dict(virtual_sio_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


