# TerminateFaultTolerantVMRequestType

The parameters of *VirtualMachine.TerminateFaultTolerantVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.terminate_fault_tolerant_vm_request_type import TerminateFaultTolerantVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateFaultTolerantVMRequestType from a JSON string
terminate_fault_tolerant_vm_request_type_instance = TerminateFaultTolerantVMRequestType.from_json(json)
# print the JSON string representation of the object
print TerminateFaultTolerantVMRequestType.to_json()

# convert the object into a dict
terminate_fault_tolerant_vm_request_type_dict = terminate_fault_tolerant_vm_request_type_instance.to_dict()
# create an instance of TerminateFaultTolerantVMRequestType from a dict
terminate_fault_tolerant_vm_request_type_form_dict = terminate_fault_tolerant_vm_request_type.from_dict(terminate_fault_tolerant_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


