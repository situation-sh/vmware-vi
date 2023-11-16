# VmDiskFileQuery

This data object type describes the query specification for the virtual disk primary file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**VmDiskFileQueryFilter**](VmDiskFileQueryFilter.md) |  | [optional] 
**details** | [**VmDiskFileQueryFlags**](VmDiskFileQueryFlags.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_disk_file_query import VmDiskFileQuery

# TODO update the JSON string below
json = "{}"
# create an instance of VmDiskFileQuery from a JSON string
vm_disk_file_query_instance = VmDiskFileQuery.from_json(json)
# print the JSON string representation of the object
print VmDiskFileQuery.to_json()

# convert the object into a dict
vm_disk_file_query_dict = vm_disk_file_query_instance.to_dict()
# create an instance of VmDiskFileQuery from a dict
vm_disk_file_query_form_dict = vm_disk_file_query.from_dict(vm_disk_file_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


