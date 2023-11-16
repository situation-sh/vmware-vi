# ArrayOfVmConfigFileQueryFilter

A boxed array of *VmConfigFileQueryFilter*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmConfigFileQueryFilter]**](VmConfigFileQueryFilter.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_config_file_query_filter import ArrayOfVmConfigFileQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmConfigFileQueryFilter from a JSON string
array_of_vm_config_file_query_filter_instance = ArrayOfVmConfigFileQueryFilter.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmConfigFileQueryFilter.to_json()

# convert the object into a dict
array_of_vm_config_file_query_filter_dict = array_of_vm_config_file_query_filter_instance.to_dict()
# create an instance of ArrayOfVmConfigFileQueryFilter from a dict
array_of_vm_config_file_query_filter_form_dict = array_of_vm_config_file_query_filter.from_dict(array_of_vm_config_file_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


