# VirtualLsiLogicController

VirtualLsiLogicController is the data object that represents a LSI Logic SCSI controller. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_lsi_logic_controller import VirtualLsiLogicController

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualLsiLogicController from a JSON string
virtual_lsi_logic_controller_instance = VirtualLsiLogicController.from_json(json)
# print the JSON string representation of the object
print VirtualLsiLogicController.to_json()

# convert the object into a dict
virtual_lsi_logic_controller_dict = virtual_lsi_logic_controller_instance.to_dict()
# create an instance of VirtualLsiLogicController from a dict
virtual_lsi_logic_controller_form_dict = virtual_lsi_logic_controller.from_dict(virtual_lsi_logic_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


