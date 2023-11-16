# ArrayOfVirtualPCIController

A boxed array of *VirtualPCIController*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualPCIController]**](VirtualPCIController.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_pci_controller import ArrayOfVirtualPCIController

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualPCIController from a JSON string
array_of_virtual_pci_controller_instance = ArrayOfVirtualPCIController.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualPCIController.to_json()

# convert the object into a dict
array_of_virtual_pci_controller_dict = array_of_virtual_pci_controller_instance.to_dict()
# create an instance of ArrayOfVirtualPCIController from a dict
array_of_virtual_pci_controller_form_dict = array_of_virtual_pci_controller.from_dict(array_of_virtual_pci_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


