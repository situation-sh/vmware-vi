# VirtualSIOControllerOption

The VirtualSIOControllerOption data object type contains the options for a virtual Super IO Controller. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_floppy_drives** | [**IntOption**](IntOption.md) |  | 
**num_serial_ports** | [**IntOption**](IntOption.md) |  | 
**num_parallel_ports** | [**IntOption**](IntOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_sio_controller_option import VirtualSIOControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSIOControllerOption from a JSON string
virtual_sio_controller_option_instance = VirtualSIOControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualSIOControllerOption.to_json()

# convert the object into a dict
virtual_sio_controller_option_dict = virtual_sio_controller_option_instance.to_dict()
# create an instance of VirtualSIOControllerOption from a dict
virtual_sio_controller_option_form_dict = virtual_sio_controller_option.from_dict(virtual_sio_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


