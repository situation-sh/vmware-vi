# VirtualLsiLogicControllerOption

VirtualLsiLogicControllerOption is the data object that contains the options for a LSI Logic SCSI controller. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_lsi_logic_controller_option import VirtualLsiLogicControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualLsiLogicControllerOption from a JSON string
virtual_lsi_logic_controller_option_instance = VirtualLsiLogicControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualLsiLogicControllerOption.to_json()

# convert the object into a dict
virtual_lsi_logic_controller_option_dict = virtual_lsi_logic_controller_option_instance.to_dict()
# create an instance of VirtualLsiLogicControllerOption from a dict
virtual_lsi_logic_controller_option_form_dict = virtual_lsi_logic_controller_option.from_dict(virtual_lsi_logic_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


