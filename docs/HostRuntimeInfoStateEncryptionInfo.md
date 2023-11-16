# HostRuntimeInfoStateEncryptionInfo

This data type describes the host's persistent state encryption.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protection_mode** | **str** | The state encryption key protection mode.  The host state is encrypted with a key that is protected using one of the modes specified by *HostRuntimeInfoStateEncryptionInfoProtectionMode_enum*.  ***Since:*** vSphere API 7.0.3.0  | 
**require_secure_boot** | **bool** | Indicates if UEFI Secure Boot must be enabled in order for the state encryption key to be accessible.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**require_exec_installed_only** | **bool** | Indicates if the \&quot;execInstalledOnly\&quot; enforcement must be active for the state encryption key to be accessible.  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.host_runtime_info_state_encryption_info import HostRuntimeInfoStateEncryptionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostRuntimeInfoStateEncryptionInfo from a JSON string
host_runtime_info_state_encryption_info_instance = HostRuntimeInfoStateEncryptionInfo.from_json(json)
# print the JSON string representation of the object
print HostRuntimeInfoStateEncryptionInfo.to_json()

# convert the object into a dict
host_runtime_info_state_encryption_info_dict = host_runtime_info_state_encryption_info_instance.to_dict()
# create an instance of HostRuntimeInfoStateEncryptionInfo from a dict
host_runtime_info_state_encryption_info_form_dict = host_runtime_info_state_encryption_info.from_dict(host_runtime_info_state_encryption_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


