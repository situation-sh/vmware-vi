# VirtualLsiLogicSASControllerOption

VirtualLsiLogicSASControllerOption is the data object that contains the options for a LSI Logic SAS SCSI controller.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_lsi_logic_sas_controller_option import VirtualLsiLogicSASControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualLsiLogicSASControllerOption from a JSON string
virtual_lsi_logic_sas_controller_option_instance = VirtualLsiLogicSASControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualLsiLogicSASControllerOption.to_json()

# convert the object into a dict
virtual_lsi_logic_sas_controller_option_dict = virtual_lsi_logic_sas_controller_option_instance.to_dict()
# create an instance of VirtualLsiLogicSASControllerOption from a dict
virtual_lsi_logic_sas_controller_option_form_dict = virtual_lsi_logic_sas_controller_option.from_dict(virtual_lsi_logic_sas_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


