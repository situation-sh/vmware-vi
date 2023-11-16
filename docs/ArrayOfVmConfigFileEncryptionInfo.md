# ArrayOfVmConfigFileEncryptionInfo

A boxed array of *VmConfigFileEncryptionInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmConfigFileEncryptionInfo]**](VmConfigFileEncryptionInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_config_file_encryption_info import ArrayOfVmConfigFileEncryptionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmConfigFileEncryptionInfo from a JSON string
array_of_vm_config_file_encryption_info_instance = ArrayOfVmConfigFileEncryptionInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmConfigFileEncryptionInfo.to_json()

# convert the object into a dict
array_of_vm_config_file_encryption_info_dict = array_of_vm_config_file_encryption_info_instance.to_dict()
# create an instance of ArrayOfVmConfigFileEncryptionInfo from a dict
array_of_vm_config_file_encryption_info_form_dict = array_of_vm_config_file_encryption_info.from_dict(array_of_vm_config_file_encryption_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


