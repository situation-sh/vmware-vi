# ArrayOfVmDiskFileInfo

A boxed array of *VmDiskFileInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmDiskFileInfo]**](VmDiskFileInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_disk_file_info import ArrayOfVmDiskFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmDiskFileInfo from a JSON string
array_of_vm_disk_file_info_instance = ArrayOfVmDiskFileInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmDiskFileInfo.to_json()

# convert the object into a dict
array_of_vm_disk_file_info_dict = array_of_vm_disk_file_info_instance.to_dict()
# create an instance of ArrayOfVmDiskFileInfo from a dict
array_of_vm_disk_file_info_form_dict = array_of_vm_disk_file_info.from_dict(array_of_vm_disk_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


