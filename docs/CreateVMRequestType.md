# CreateVMRequestType

The parameters of *Folder.CreateVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**VirtualMachineConfigSpec**](VirtualMachineConfigSpec.md) |  | 
**pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.create_vm_request_type import CreateVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVMRequestType from a JSON string
create_vm_request_type_instance = CreateVMRequestType.from_json(json)
# print the JSON string representation of the object
print CreateVMRequestType.to_json()

# convert the object into a dict
create_vm_request_type_dict = create_vm_request_type_instance.to_dict()
# create an instance of CreateVMRequestType from a dict
create_vm_request_type_form_dict = create_vm_request_type.from_dict(create_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


