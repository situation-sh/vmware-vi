# VirtualAHCIController

The VirtualAHCIController data object type represents an AHCI SATA controller in a virtual machine.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_ahci_controller import VirtualAHCIController

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualAHCIController from a JSON string
virtual_ahci_controller_instance = VirtualAHCIController.from_json(json)
# print the JSON string representation of the object
print VirtualAHCIController.to_json()

# convert the object into a dict
virtual_ahci_controller_dict = virtual_ahci_controller_instance.to_dict()
# create an instance of VirtualAHCIController from a dict
virtual_ahci_controller_form_dict = virtual_ahci_controller.from_dict(virtual_ahci_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


