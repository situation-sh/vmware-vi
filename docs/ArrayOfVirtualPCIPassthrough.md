# ArrayOfVirtualPCIPassthrough

A boxed array of *VirtualPCIPassthrough*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualPCIPassthrough]**](VirtualPCIPassthrough.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_pci_passthrough import ArrayOfVirtualPCIPassthrough

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualPCIPassthrough from a JSON string
array_of_virtual_pci_passthrough_instance = ArrayOfVirtualPCIPassthrough.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualPCIPassthrough.to_json()

# convert the object into a dict
array_of_virtual_pci_passthrough_dict = array_of_virtual_pci_passthrough_instance.to_dict()
# create an instance of ArrayOfVirtualPCIPassthrough from a dict
array_of_virtual_pci_passthrough_form_dict = array_of_virtual_pci_passthrough.from_dict(array_of_virtual_pci_passthrough_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


