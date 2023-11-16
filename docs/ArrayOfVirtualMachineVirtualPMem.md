# ArrayOfVirtualMachineVirtualPMem

A boxed array of *VirtualMachineVirtualPMem*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineVirtualPMem]**](VirtualMachineVirtualPMem.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_virtual_p_mem import ArrayOfVirtualMachineVirtualPMem

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineVirtualPMem from a JSON string
array_of_virtual_machine_virtual_p_mem_instance = ArrayOfVirtualMachineVirtualPMem.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineVirtualPMem.to_json()

# convert the object into a dict
array_of_virtual_machine_virtual_p_mem_dict = array_of_virtual_machine_virtual_p_mem_instance.to_dict()
# create an instance of ArrayOfVirtualMachineVirtualPMem from a dict
array_of_virtual_machine_virtual_p_mem_form_dict = array_of_virtual_machine_virtual_p_mem.from_dict(array_of_virtual_machine_virtual_p_mem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


