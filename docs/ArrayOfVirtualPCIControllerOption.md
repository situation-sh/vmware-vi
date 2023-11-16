# ArrayOfVirtualPCIControllerOption

A boxed array of *VirtualPCIControllerOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualPCIControllerOption]**](VirtualPCIControllerOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_pci_controller_option import ArrayOfVirtualPCIControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualPCIControllerOption from a JSON string
array_of_virtual_pci_controller_option_instance = ArrayOfVirtualPCIControllerOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualPCIControllerOption.to_json()

# convert the object into a dict
array_of_virtual_pci_controller_option_dict = array_of_virtual_pci_controller_option_instance.to_dict()
# create an instance of ArrayOfVirtualPCIControllerOption from a dict
array_of_virtual_pci_controller_option_form_dict = array_of_virtual_pci_controller_option.from_dict(array_of_virtual_pci_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


