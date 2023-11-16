# MakePrimaryVMRequestType

The parameters of *VirtualMachine.MakePrimaryVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.make_primary_vm_request_type import MakePrimaryVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MakePrimaryVMRequestType from a JSON string
make_primary_vm_request_type_instance = MakePrimaryVMRequestType.from_json(json)
# print the JSON string representation of the object
print MakePrimaryVMRequestType.to_json()

# convert the object into a dict
make_primary_vm_request_type_dict = make_primary_vm_request_type_instance.to_dict()
# create an instance of MakePrimaryVMRequestType from a dict
make_primary_vm_request_type_form_dict = make_primary_vm_request_type.from_dict(make_primary_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


