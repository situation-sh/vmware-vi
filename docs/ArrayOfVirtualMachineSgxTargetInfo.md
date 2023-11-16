# ArrayOfVirtualMachineSgxTargetInfo

A boxed array of *VirtualMachineSgxTargetInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineSgxTargetInfo]**](VirtualMachineSgxTargetInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_sgx_target_info import ArrayOfVirtualMachineSgxTargetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineSgxTargetInfo from a JSON string
array_of_virtual_machine_sgx_target_info_instance = ArrayOfVirtualMachineSgxTargetInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineSgxTargetInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_sgx_target_info_dict = array_of_virtual_machine_sgx_target_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineSgxTargetInfo from a dict
array_of_virtual_machine_sgx_target_info_form_dict = array_of_virtual_machine_sgx_target_info.from_dict(array_of_virtual_machine_sgx_target_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


