# VmConfigFileQueryFlags


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_version** | **bool** | The flag to indicate whether or not the configuration file version number is returned.  | 
**encryption** | **bool** | The flag to indicate whether the encryption information of the virtual machine configuration is returned.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.vm_config_file_query_flags import VmConfigFileQueryFlags

# TODO update the JSON string below
json = "{}"
# create an instance of VmConfigFileQueryFlags from a JSON string
vm_config_file_query_flags_instance = VmConfigFileQueryFlags.from_json(json)
# print the JSON string representation of the object
print VmConfigFileQueryFlags.to_json()

# convert the object into a dict
vm_config_file_query_flags_dict = vm_config_file_query_flags_instance.to_dict()
# create an instance of VmConfigFileQueryFlags from a dict
vm_config_file_query_flags_form_dict = vm_config_file_query_flags.from_dict(vm_config_file_query_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


