# ArrayOfVmDiskFileQueryFlags

A boxed array of *VmDiskFileQueryFlags*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmDiskFileQueryFlags]**](VmDiskFileQueryFlags.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_disk_file_query_flags import ArrayOfVmDiskFileQueryFlags

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmDiskFileQueryFlags from a JSON string
array_of_vm_disk_file_query_flags_instance = ArrayOfVmDiskFileQueryFlags.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmDiskFileQueryFlags.to_json()

# convert the object into a dict
array_of_vm_disk_file_query_flags_dict = array_of_vm_disk_file_query_flags_instance.to_dict()
# create an instance of ArrayOfVmDiskFileQueryFlags from a dict
array_of_vm_disk_file_query_flags_form_dict = array_of_vm_disk_file_query_flags.from_dict(array_of_vm_disk_file_query_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


