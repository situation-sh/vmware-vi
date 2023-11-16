# RegisterVMRequestType

The parameters of *Folder.RegisterVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | A datastore path to the virtual machine.  | 
**name** | **str** | The name to be assigned to the virtual machine. If this parameter is not set, the displayName configuration parameter of the virtual machine is used. An entity name must be a non-empty string of less than 80 characters. The slash (/), backslash (\\\\) and percent (%) will be escaped using the URL syntax. For example, %2F.  | [optional] 
**as_template** | **bool** | Flag to specify whether or not the virtual machine should be marked as a template.  | 
**pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.register_vm_request_type import RegisterVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterVMRequestType from a JSON string
register_vm_request_type_instance = RegisterVMRequestType.from_json(json)
# print the JSON string representation of the object
print RegisterVMRequestType.to_json()

# convert the object into a dict
register_vm_request_type_dict = register_vm_request_type_instance.to_dict()
# create an instance of RegisterVMRequestType from a dict
register_vm_request_type_form_dict = register_vm_request_type.from_dict(register_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


