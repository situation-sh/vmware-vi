# CreateChildVMRequestType

The parameters of *ResourcePool.CreateChildVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**VirtualMachineConfigSpec**](VirtualMachineConfigSpec.md) |  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.create_child_vm_request_type import CreateChildVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateChildVMRequestType from a JSON string
create_child_vm_request_type_instance = CreateChildVMRequestType.from_json(json)
# print the JSON string representation of the object
print CreateChildVMRequestType.to_json()

# convert the object into a dict
create_child_vm_request_type_dict = create_child_vm_request_type_instance.to_dict()
# create an instance of CreateChildVMRequestType from a dict
create_child_vm_request_type_form_dict = create_child_vm_request_type.from_dict(create_child_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


