# VirtualMachineVFlashModuleInfo

VFlashModuleInfo class contains information about a vFlash module on the host.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**v_flash_module** | [**HostVFlashManagerVFlashCacheConfigInfoVFlashModuleConfigOption**](HostVFlashManagerVFlashCacheConfigInfoVFlashModuleConfigOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_machine_v_flash_module_info import VirtualMachineVFlashModuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineVFlashModuleInfo from a JSON string
virtual_machine_v_flash_module_info_instance = VirtualMachineVFlashModuleInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineVFlashModuleInfo.to_json()

# convert the object into a dict
virtual_machine_v_flash_module_info_dict = virtual_machine_v_flash_module_info_instance.to_dict()
# create an instance of VirtualMachineVFlashModuleInfo from a dict
virtual_machine_v_flash_module_info_form_dict = virtual_machine_v_flash_module_info.from_dict(virtual_machine_v_flash_module_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


