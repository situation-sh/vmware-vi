# ArrayOfKernelModuleInfo

A boxed array of *KernelModuleInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[KernelModuleInfo]**](KernelModuleInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_kernel_module_info import ArrayOfKernelModuleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfKernelModuleInfo from a JSON string
array_of_kernel_module_info_instance = ArrayOfKernelModuleInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfKernelModuleInfo.to_json()

# convert the object into a dict
array_of_kernel_module_info_dict = array_of_kernel_module_info_instance.to_dict()
# create an instance of ArrayOfKernelModuleInfo from a dict
array_of_kernel_module_info_form_dict = array_of_kernel_module_info.from_dict(array_of_kernel_module_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


