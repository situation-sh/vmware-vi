# RelocateVMRequestType

The parameters of *VirtualMachine.RelocateVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**VirtualMachineRelocateSpec**](VirtualMachineRelocateSpec.md) |  | 
**priority** | [**VirtualMachineMovePriorityEnum**](VirtualMachineMovePriorityEnum.md) |  | [optional] 

## Example

```python
from vmware_vi.models.relocate_vm_request_type import RelocateVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RelocateVMRequestType from a JSON string
relocate_vm_request_type_instance = RelocateVMRequestType.from_json(json)
# print the JSON string representation of the object
print RelocateVMRequestType.to_json()

# convert the object into a dict
relocate_vm_request_type_dict = relocate_vm_request_type_instance.to_dict()
# create an instance of RelocateVMRequestType from a dict
relocate_vm_request_type_form_dict = relocate_vm_request_type.from_dict(relocate_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


