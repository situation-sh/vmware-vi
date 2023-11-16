# VirtualIDEControllerOption

The VirtualIDEControllerOption data object type contains the options for a virtual IDE controller. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_ide_disks** | [**IntOption**](IntOption.md) |  | 
**num_ide_cdroms** | [**IntOption**](IntOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_ide_controller_option import VirtualIDEControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualIDEControllerOption from a JSON string
virtual_ide_controller_option_instance = VirtualIDEControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualIDEControllerOption.to_json()

# convert the object into a dict
virtual_ide_controller_option_dict = virtual_ide_controller_option_instance.to_dict()
# create an instance of VirtualIDEControllerOption from a dict
virtual_ide_controller_option_form_dict = virtual_ide_controller_option.from_dict(virtual_ide_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


