# VirtualAHCIControllerOption

VirtualAHCIControllerOption is the data object that contains the options for an AHCI SATA controller.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_ahci_controller_option import VirtualAHCIControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAHCIControllerOption from a JSON string
virtual_ahci_controller_option_instance = VirtualAHCIControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualAHCIControllerOption.to_json()

# convert the object into a dict
virtual_ahci_controller_option_dict = virtual_ahci_controller_option_instance.to_dict()
# create an instance of VirtualAHCIControllerOption from a dict
virtual_ahci_controller_option_form_dict = virtual_ahci_controller_option.from_dict(virtual_ahci_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


