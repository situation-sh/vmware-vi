# ArrayOfVirtualMachineVFlashModuleInfo

A boxed array of *VirtualMachineVFlashModuleInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineVFlashModuleInfo]**](VirtualMachineVFlashModuleInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_v_flash_module_info import ArrayOfVirtualMachineVFlashModuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineVFlashModuleInfo from a JSON string
array_of_virtual_machine_v_flash_module_info_instance = ArrayOfVirtualMachineVFlashModuleInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineVFlashModuleInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_v_flash_module_info_dict = array_of_virtual_machine_v_flash_module_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineVFlashModuleInfo from a dict
array_of_virtual_machine_v_flash_module_info_form_dict = array_of_virtual_machine_v_flash_module_info.from_dict(array_of_virtual_machine_v_flash_module_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


