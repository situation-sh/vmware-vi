# ReconfigVMRequestType

The parameters of *VirtualMachine.ReconfigVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**VirtualMachineConfigSpec**](VirtualMachineConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.reconfig_vm_request_type import ReconfigVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigVMRequestType from a JSON string
reconfig_vm_request_type_instance = ReconfigVMRequestType.from_json(json)
# print the JSON string representation of the object
print ReconfigVMRequestType.to_json()

# convert the object into a dict
reconfig_vm_request_type_dict = reconfig_vm_request_type_instance.to_dict()
# create an instance of ReconfigVMRequestType from a dict
reconfig_vm_request_type_form_dict = reconfig_vm_request_type.from_dict(reconfig_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


