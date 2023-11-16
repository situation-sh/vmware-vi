# VmConfigFileQueryFilter

The filter for the virtual machine configuration file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_config_version** | **List[int]** | If this property is set, only the virtual machine configuration files that match one of the specified configuration versions are selected.  If no versions are specified, this search criteria is ignored.  | [optional] 
**encrypted** | **bool** | This optional property can be used to filter virtual machine configuration files based on whether they are encrypted or not.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.vm_config_file_query_filter import VmConfigFileQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of VmConfigFileQueryFilter from a JSON string
vm_config_file_query_filter_instance = VmConfigFileQueryFilter.from_json(json)
# print the JSON string representation of the object
print VmConfigFileQueryFilter.to_json()

# convert the object into a dict
vm_config_file_query_filter_dict = vm_config_file_query_filter_instance.to_dict()
# create an instance of VmConfigFileQueryFilter from a dict
vm_config_file_query_filter_form_dict = vm_config_file_query_filter.from_dict(vm_config_file_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


