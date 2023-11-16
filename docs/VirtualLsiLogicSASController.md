# VirtualLsiLogicSASController

VirtualLsiLogicSASController is the data object that represents a LSI Logic SAS SCSI controller.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_lsi_logic_sas_controller import VirtualLsiLogicSASController

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualLsiLogicSASController from a JSON string
virtual_lsi_logic_sas_controller_instance = VirtualLsiLogicSASController.from_json(json)
# print the JSON string representation of the object
print VirtualLsiLogicSASController.to_json()

# convert the object into a dict
virtual_lsi_logic_sas_controller_dict = virtual_lsi_logic_sas_controller_instance.to_dict()
# create an instance of VirtualLsiLogicSASController from a dict
virtual_lsi_logic_sas_controller_form_dict = virtual_lsi_logic_sas_controller.from_dict(virtual_lsi_logic_sas_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


