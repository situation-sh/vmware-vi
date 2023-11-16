# VirtualPCIPassthrough

The VirtualPCIPassthrough data object type contains information about a PCI device on the virtual machine that is being backed by a generic PCI device on the host via passthrough.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_pci_passthrough import VirtualPCIPassthrough

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualPCIPassthrough from a JSON string
virtual_pci_passthrough_instance = VirtualPCIPassthrough.from_json(json)
# print the JSON string representation of the object
print VirtualPCIPassthrough.to_json()

# convert the object into a dict
virtual_pci_passthrough_dict = virtual_pci_passthrough_instance.to_dict()
# create an instance of VirtualPCIPassthrough from a dict
virtual_pci_passthrough_form_dict = virtual_pci_passthrough.from_dict(virtual_pci_passthrough_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


