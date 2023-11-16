# VmLogFileInfo

This data object type describes a file that is logging output for a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_log_file_info import VmLogFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VmLogFileInfo from a JSON string
vm_log_file_info_instance = VmLogFileInfo.from_json(json)
# print the JSON string representation of the object
print VmLogFileInfo.to_json()

# convert the object into a dict
vm_log_file_info_dict = vm_log_file_info_instance.to_dict()
# create an instance of VmLogFileInfo from a dict
vm_log_file_info_form_dict = vm_log_file_info.from_dict(vm_log_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


