# ArrayOfVirtualMachineVMIROM

A boxed array of *VirtualMachineVMIROM*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineVMIROM]**](VirtualMachineVMIROM.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_vmirom import ArrayOfVirtualMachineVMIROM

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineVMIROM from a JSON string
array_of_virtual_machine_vmirom_instance = ArrayOfVirtualMachineVMIROM.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineVMIROM.to_json()

# convert the object into a dict
array_of_virtual_machine_vmirom_dict = array_of_virtual_machine_vmirom_instance.to_dict()
# create an instance of ArrayOfVirtualMachineVMIROM from a dict
array_of_virtual_machine_vmirom_form_dict = array_of_virtual_machine_vmirom.from_dict(array_of_virtual_machine_vmirom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


