# ArrayOfVmLogFileQuery

A boxed array of *VmLogFileQuery*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmLogFileQuery]**](VmLogFileQuery.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_log_file_query import ArrayOfVmLogFileQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmLogFileQuery from a JSON string
array_of_vm_log_file_query_instance = ArrayOfVmLogFileQuery.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmLogFileQuery.to_json()

# convert the object into a dict
array_of_vm_log_file_query_dict = array_of_vm_log_file_query_instance.to_dict()
# create an instance of ArrayOfVmLogFileQuery from a dict
array_of_vm_log_file_query_form_dict = array_of_vm_log_file_query.from_dict(array_of_vm_log_file_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


