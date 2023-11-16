# CloneVMRequestType

The parameters of *VirtualMachine.CloneVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**name** | **str** | The name of the new virtual machine.  | 
**spec** | [**VirtualMachineCloneSpec**](VirtualMachineCloneSpec.md) |  | 

## Example

```python
from vmware_vi.models.clone_vm_request_type import CloneVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CloneVMRequestType from a JSON string
clone_vm_request_type_instance = CloneVMRequestType.from_json(json)
# print the JSON string representation of the object
print CloneVMRequestType.to_json()

# convert the object into a dict
clone_vm_request_type_dict = clone_vm_request_type_instance.to_dict()
# create an instance of CloneVMRequestType from a dict
clone_vm_request_type_form_dict = clone_vm_request_type.from_dict(clone_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


