# RegisterChildVMRequestType

The parameters of *ResourcePool.RegisterChildVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | A datastore path to the virtual machine. If the path ends with \&quot;.vmtx\&quot;, indicating that it refers to a VM template, an InvalidArgument fault is thrown.  | 
**name** | **str** | The name to be assigned to the virtual machine. If this parameter is not set, the displayName configuration parameter of the virtual machine is used. An entity name must be a non-empty string of less than 80 characters. The slash (/), backslash (\\\\) and percent (%) will be escaped using the URL syntax. For example, %2F.  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.register_child_vm_request_type import RegisterChildVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterChildVMRequestType from a JSON string
register_child_vm_request_type_instance = RegisterChildVMRequestType.from_json(json)
# print the JSON string representation of the object
print RegisterChildVMRequestType.to_json()

# convert the object into a dict
register_child_vm_request_type_dict = register_child_vm_request_type_instance.to_dict()
# create an instance of RegisterChildVMRequestType from a dict
register_child_vm_request_type_form_dict = register_child_vm_request_type.from_dict(register_child_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


