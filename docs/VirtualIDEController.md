# VirtualIDEController

The VirtualIDEController data object type specifies a virtual IDE controller. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_ide_controller import VirtualIDEController

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualIDEController from a JSON string
virtual_ide_controller_instance = VirtualIDEController.from_json(json)
# print the JSON string representation of the object
print VirtualIDEController.to_json()

# convert the object into a dict
virtual_ide_controller_dict = virtual_ide_controller_instance.to_dict()
# create an instance of VirtualIDEController from a dict
virtual_ide_controller_form_dict = virtual_ide_controller.from_dict(virtual_ide_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


