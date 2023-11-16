# ArrayOfVmDiskFileQueryFilter

A boxed array of *VmDiskFileQueryFilter*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmDiskFileQueryFilter]**](VmDiskFileQueryFilter.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_disk_file_query_filter import ArrayOfVmDiskFileQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmDiskFileQueryFilter from a JSON string
array_of_vm_disk_file_query_filter_instance = ArrayOfVmDiskFileQueryFilter.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmDiskFileQueryFilter.to_json()

# convert the object into a dict
array_of_vm_disk_file_query_filter_dict = array_of_vm_disk_file_query_filter_instance.to_dict()
# create an instance of ArrayOfVmDiskFileQueryFilter from a dict
array_of_vm_disk_file_query_filter_form_dict = array_of_vm_disk_file_query_filter.from_dict(array_of_vm_disk_file_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


