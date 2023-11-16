# ArrayOfVmLogFileInfo

A boxed array of *VmLogFileInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmLogFileInfo]**](VmLogFileInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_log_file_info import ArrayOfVmLogFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmLogFileInfo from a JSON string
array_of_vm_log_file_info_instance = ArrayOfVmLogFileInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmLogFileInfo.to_json()

# convert the object into a dict
array_of_vm_log_file_info_dict = array_of_vm_log_file_info_instance.to_dict()
# create an instance of ArrayOfVmLogFileInfo from a dict
array_of_vm_log_file_info_form_dict = array_of_vm_log_file_info.from_dict(array_of_vm_log_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


