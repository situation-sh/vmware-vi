# KernelModuleSectionInfo

Information about a module section.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **int** | Base address of section.  ***Since:*** vSphere API 4.0  | 
**length** | **int** | Section length.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.kernel_module_section_info import KernelModuleSectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KernelModuleSectionInfo from a JSON string
kernel_module_section_info_instance = KernelModuleSectionInfo.from_json(json)
# print the JSON string representation of the object
print KernelModuleSectionInfo.to_json()

# convert the object into a dict
kernel_module_section_info_dict = kernel_module_section_info_instance.to_dict()
# create an instance of KernelModuleSectionInfo from a dict
kernel_module_section_info_form_dict = kernel_module_section_info.from_dict(kernel_module_section_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


