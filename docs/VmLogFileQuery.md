# VmLogFileQuery

This data object type describes the query specification for a virtual machine log file file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_log_file_query import VmLogFileQuery

# TODO update the JSON string below
json = "{}"
# create an instance of VmLogFileQuery from a JSON string
vm_log_file_query_instance = VmLogFileQuery.from_json(json)
# print the JSON string representation of the object
print VmLogFileQuery.to_json()

# convert the object into a dict
vm_log_file_query_dict = vm_log_file_query_instance.to_dict()
# create an instance of VmLogFileQuery from a dict
vm_log_file_query_form_dict = vm_log_file_query.from_dict(vm_log_file_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


