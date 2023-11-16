# VmConfigFileEncryptionInfo

The encryption information of a virtual machine configuration.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_config_file_encryption_info import VmConfigFileEncryptionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VmConfigFileEncryptionInfo from a JSON string
vm_config_file_encryption_info_instance = VmConfigFileEncryptionInfo.from_json(json)
# print the JSON string representation of the object
print VmConfigFileEncryptionInfo.to_json()

# convert the object into a dict
vm_config_file_encryption_info_dict = vm_config_file_encryption_info_instance.to_dict()
# create an instance of VmConfigFileEncryptionInfo from a dict
vm_config_file_encryption_info_form_dict = vm_config_file_encryption_info.from_dict(vm_config_file_encryption_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


