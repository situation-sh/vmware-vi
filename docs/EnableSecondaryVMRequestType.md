# EnableSecondaryVMRequestType

The parameters of *VirtualMachine.EnableSecondaryVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.enable_secondary_vm_request_type import EnableSecondaryVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EnableSecondaryVMRequestType from a JSON string
enable_secondary_vm_request_type_instance = EnableSecondaryVMRequestType.from_json(json)
# print the JSON string representation of the object
print EnableSecondaryVMRequestType.to_json()

# convert the object into a dict
enable_secondary_vm_request_type_dict = enable_secondary_vm_request_type_instance.to_dict()
# create an instance of EnableSecondaryVMRequestType from a dict
enable_secondary_vm_request_type_form_dict = enable_secondary_vm_request_type.from_dict(enable_secondary_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


