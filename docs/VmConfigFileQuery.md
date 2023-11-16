# VmConfigFileQuery

This data object type describes query specification for the virtual machine configuration file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**VmConfigFileQueryFilter**](VmConfigFileQueryFilter.md) |  | [optional] 
**details** | [**VmConfigFileQueryFlags**](VmConfigFileQueryFlags.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_config_file_query import VmConfigFileQuery

# TODO update the JSON string below
json = "{}"
# create an instance of VmConfigFileQuery from a JSON string
vm_config_file_query_instance = VmConfigFileQuery.from_json(json)
# print the JSON string representation of the object
print VmConfigFileQuery.to_json()

# convert the object into a dict
vm_config_file_query_dict = vm_config_file_query_instance.to_dict()
# create an instance of VmConfigFileQuery from a dict
vm_config_file_query_form_dict = vm_config_file_query.from_dict(vm_config_file_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


