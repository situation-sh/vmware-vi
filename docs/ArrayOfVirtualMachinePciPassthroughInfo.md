# ArrayOfVirtualMachinePciPassthroughInfo

A boxed array of *VirtualMachinePciPassthroughInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachinePciPassthroughInfo]**](VirtualMachinePciPassthroughInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_pci_passthrough_info import ArrayOfVirtualMachinePciPassthroughInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachinePciPassthroughInfo from a JSON string
array_of_virtual_machine_pci_passthrough_info_instance = ArrayOfVirtualMachinePciPassthroughInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachinePciPassthroughInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_pci_passthrough_info_dict = array_of_virtual_machine_pci_passthrough_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachinePciPassthroughInfo from a dict
array_of_virtual_machine_pci_passthrough_info_form_dict = array_of_virtual_machine_pci_passthrough_info.from_dict(array_of_virtual_machine_pci_passthrough_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


