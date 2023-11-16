# VirtualMachineVMIROM

Deprecated as of vSphere API 6.0. On vSphere 6.0 and later platforms, the VMIROM device does not provide any functionality.  The VirtualVMIROM data object type represents the ROM on the virtual machine's PCI bus that provides support for VMI.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_machine_vmirom import VirtualMachineVMIROM

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVMIROM from a JSON string
virtual_machine_vmirom_instance = VirtualMachineVMIROM.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVMIROM.to_json()

# convert the object into a dict
virtual_machine_vmirom_dict = virtual_machine_vmirom_instance.to_dict()
# create an instance of VirtualMachineVMIROM from a dict
virtual_machine_vmirom_form_dict = virtual_machine_vmirom.from_dict(virtual_machine_vmirom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


