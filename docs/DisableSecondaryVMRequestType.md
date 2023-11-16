# DisableSecondaryVMRequestType

The parameters of *VirtualMachine.DisableSecondaryVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.disable_secondary_vm_request_type import DisableSecondaryVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DisableSecondaryVMRequestType from a JSON string
disable_secondary_vm_request_type_instance = DisableSecondaryVMRequestType.from_json(json)
# print the JSON string representation of the object
print DisableSecondaryVMRequestType.to_json()

# convert the object into a dict
disable_secondary_vm_request_type_dict = disable_secondary_vm_request_type_instance.to_dict()
# create an instance of DisableSecondaryVMRequestType from a dict
disable_secondary_vm_request_type_form_dict = disable_secondary_vm_request_type.from_dict(disable_secondary_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


