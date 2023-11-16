# MigrateVMRequestType

The parameters of *VirtualMachine.MigrateVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**priority** | [**VirtualMachineMovePriorityEnum**](VirtualMachineMovePriorityEnum.md) |  | 
**state** | [**VirtualMachinePowerStateEnum**](VirtualMachinePowerStateEnum.md) |  | [optional] 

## Example

```python
from vmware_vi.models.migrate_vm_request_type import MigrateVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MigrateVMRequestType from a JSON string
migrate_vm_request_type_instance = MigrateVMRequestType.from_json(json)
# print the JSON string representation of the object
print MigrateVMRequestType.to_json()

# convert the object into a dict
migrate_vm_request_type_dict = migrate_vm_request_type_instance.to_dict()
# create an instance of MigrateVMRequestType from a dict
migrate_vm_request_type_form_dict = migrate_vm_request_type.from_dict(migrate_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


