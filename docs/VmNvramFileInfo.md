# VmNvramFileInfo

This data object type describes a file that is a virtual machine non-volatile memory file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_nvram_file_info import VmNvramFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VmNvramFileInfo from a JSON string
vm_nvram_file_info_instance = VmNvramFileInfo.from_json(json)
# print the JSON string representation of the object
print VmNvramFileInfo.to_json()

# convert the object into a dict
vm_nvram_file_info_dict = vm_nvram_file_info_instance.to_dict()
# create an instance of VmNvramFileInfo from a dict
vm_nvram_file_info_form_dict = vm_nvram_file_info.from_dict(vm_nvram_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


