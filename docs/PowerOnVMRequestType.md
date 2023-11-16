# PowerOnVMRequestType

The parameters of *VirtualMachine.PowerOnVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.power_on_vm_request_type import PowerOnVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of PowerOnVMRequestType from a JSON string
power_on_vm_request_type_instance = PowerOnVMRequestType.from_json(json)
# print the JSON string representation of the object
print PowerOnVMRequestType.to_json()

# convert the object into a dict
power_on_vm_request_type_dict = power_on_vm_request_type_instance.to_dict()
# create an instance of PowerOnVMRequestType from a dict
power_on_vm_request_type_form_dict = power_on_vm_request_type.from_dict(power_on_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


