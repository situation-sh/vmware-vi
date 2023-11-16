# VmConfigFileInfo

This data object type describes a virtual machine configuration file. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_version** | **int** |  | [optional] 
**encryption** | [**VmConfigFileEncryptionInfo**](VmConfigFileEncryptionInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_config_file_info import VmConfigFileInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VmConfigFileInfo from a JSON string
vm_config_file_info_instance = VmConfigFileInfo.from_json(json)
# print the JSON string representation of the object
print VmConfigFileInfo.to_json()

# convert the object into a dict
vm_config_file_info_dict = vm_config_file_info_instance.to_dict()
# create an instance of VmConfigFileInfo from a dict
vm_config_file_info_form_dict = vm_config_file_info.from_dict(vm_config_file_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


