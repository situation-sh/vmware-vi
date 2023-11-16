# VirtualPCIController

The VirtualPCIController data object type defines a virtual PCI controller. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_pci_controller import VirtualPCIController

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCIController from a JSON string
virtual_pci_controller_instance = VirtualPCIController.from_json(json)
# print the JSON string representation of the object
print VirtualPCIController.to_json()

# convert the object into a dict
virtual_pci_controller_dict = virtual_pci_controller_instance.to_dict()
# create an instance of VirtualPCIController from a dict
virtual_pci_controller_form_dict = virtual_pci_controller.from_dict(virtual_pci_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


