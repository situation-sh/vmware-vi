# CustomizeVMRequestType

The parameters of *VirtualMachine.CustomizeVM_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**CustomizationSpec**](CustomizationSpec.md) |  | 

## Example

```python
from vmware_vi.models.customize_vm_request_type import CustomizeVMRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizeVMRequestType from a JSON string
customize_vm_request_type_instance = CustomizeVMRequestType.from_json(json)
# print the JSON string representation of the object
print CustomizeVMRequestType.to_json()

# convert the object into a dict
customize_vm_request_type_dict = customize_vm_request_type_instance.to_dict()
# create an instance of CustomizeVMRequestType from a dict
customize_vm_request_type_form_dict = customize_vm_request_type.from_dict(customize_vm_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


