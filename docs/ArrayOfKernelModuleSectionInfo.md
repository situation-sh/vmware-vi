# ArrayOfKernelModuleSectionInfo

A boxed array of *KernelModuleSectionInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[KernelModuleSectionInfo]**](KernelModuleSectionInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_kernel_module_section_info import ArrayOfKernelModuleSectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfKernelModuleSectionInfo from a JSON string
array_of_kernel_module_section_info_instance = ArrayOfKernelModuleSectionInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfKernelModuleSectionInfo.to_json()

# convert the object into a dict
array_of_kernel_module_section_info_dict = array_of_kernel_module_section_info_instance.to_dict()
# create an instance of ArrayOfKernelModuleSectionInfo from a dict
array_of_kernel_module_section_info_form_dict = array_of_kernel_module_section_info.from_dict(array_of_kernel_module_section_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


