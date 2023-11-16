# ToolsConfigInfo

ToolsConfigInfo is a data object type containing settings for the VMware Tools software running in the guest operating system. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tools_version** | **int** | Version of VMware Tools installed on the guest operating system.  | [optional] 
**tools_install_type** | **str** | Installation type of VMware Tools in the guest operating system.  The set of possible values is described in *VirtualMachineToolsInstallType_enum*  ***Since:*** vSphere API 6.5  | [optional] 
**after_power_on** | **bool** | Flag to specify whether or not scripts should run after the virtual machine powers on.  | [optional] 
**after_resume** | **bool** | Flag to specify whether or not scripts should run after the virtual machine resumes.  | [optional] 
**before_guest_standby** | **bool** | Flag to specify whether or not scripts should run before the virtual machine suspends.  | [optional] 
**before_guest_shutdown** | **bool** | Flag to specify whether or not scripts should run before the virtual machine powers off.  | [optional] 
**before_guest_reboot** | **bool** | Flag to specify whether or not scripts should run before the virtual machine reboots.  | [optional] 
**tools_upgrade_policy** | **str** | Tools upgrade policy setting for the virtual machine.  See also *UpgradePolicy_enum*.  ***Since:*** VI API 2.5  | [optional] 
**pending_customization** | **str** | When set, this indicates that a customization operation is pending on the VM.  The value represents the filename of the customization package on the host.  ***Since:*** VI API 2.5  | [optional] 
**customization_key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | [optional] 
**sync_time_with_host_allowed** | **bool** | Indicates whether or not the tools program is allowed to synchronize guest time with host time.  When set to &lt;code&gt;false&lt;/code&gt;, disallows tool periodic time synchronization as well as guest time step corrections due to one-off events like resume from suspend.  ***Since:*** vSphere API 7.0.1.0  | [optional] 
**sync_time_with_host** | **bool** | Flag to specify whether or not the tools program will periodically synchronize guest time with host time.  Periodical synchronization is only allowed if *ToolsConfigInfo.syncTimeWithHostAllowed* is not set to &lt;code&gt;false&lt;/code&gt;.  ***Since:*** VI API 2.5  | [optional] 
**last_install_info** | [**ToolsConfigInfoToolsLastInstallInfo**](ToolsConfigInfoToolsLastInstallInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.tools_config_info import ToolsConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsConfigInfo from a JSON string
tools_config_info_instance = ToolsConfigInfo.from_json(json)
# print the JSON string representation of the object
print ToolsConfigInfo.to_json()

# convert the object into a dict
tools_config_info_dict = tools_config_info_instance.to_dict()
# create an instance of ToolsConfigInfo from a dict
tools_config_info_form_dict = tools_config_info.from_dict(tools_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


