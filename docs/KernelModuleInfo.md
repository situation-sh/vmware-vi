# KernelModuleInfo

Information about a kernel module.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Module ID.  ***Since:*** vSphere API 4.0  | 
**name** | **str** | Module name.  ***Since:*** vSphere API 4.0  | 
**version** | **str** | Version string.  ***Since:*** vSphere API 4.0  | 
**filename** | **str** | Module filename, without the path.  ***Since:*** vSphere API 4.0  | 
**option_string** | **str** | Option string configured to be passed to the kernel module when loaded.  Note that this is not necessarily the option string currently in use by the kernel module.  ***Since:*** vSphere API 4.0  | 
**loaded** | **bool** | Is the module loaded?  ***Since:*** vSphere API 4.0  | 
**enabled** | **bool** | Is the module enabled?  ***Since:*** vSphere API 4.0  | 
**use_count** | **int** | Number of references to this module.  ***Since:*** vSphere API 4.0  | 
**read_only_section** | [**KernelModuleSectionInfo**](KernelModuleSectionInfo.md) |  | 
**writable_section** | [**KernelModuleSectionInfo**](KernelModuleSectionInfo.md) |  | 
**text_section** | [**KernelModuleSectionInfo**](KernelModuleSectionInfo.md) |  | 
**data_section** | [**KernelModuleSectionInfo**](KernelModuleSectionInfo.md) |  | 
**bss_section** | [**KernelModuleSectionInfo**](KernelModuleSectionInfo.md) |  | 

## Example

```python
from vmware_vi.models.kernel_module_info import KernelModuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KernelModuleInfo from a JSON string
kernel_module_info_instance = KernelModuleInfo.from_json(json)
# print the JSON string representation of the object
print KernelModuleInfo.to_json()

# convert the object into a dict
kernel_module_info_dict = kernel_module_info_instance.to_dict()
# create an instance of KernelModuleInfo from a dict
kernel_module_info_form_dict = kernel_module_info.from_dict(kernel_module_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


