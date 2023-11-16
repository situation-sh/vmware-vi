# HostPatchManagerStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this update.  | 
**applicable** | **bool** | Whether or not this update is applicable to this host.  An update may not be applicable to the ESX host for many reasons - for example, it is obsolete, it conflicts with other installed patches or libraries, and so on. The *HostPatchManagerStatus.reason* shows some of the reasons why the update is not applicable. An update could be inapplicable with no reason listed. This is because the prerequisite install state is not correct. For example, update A is one of the prerequisites of update B. B not only requires A to be installed, but also requires the host is rebooted after A is installed. When A is installed and the host has not been restarted after the installation, B will not be applicable. In such a case, the scan on both updates A and B would yield a whole picture of the update applicable status.  | 
**reason** | **List[str]** | Possible reasons why an update is not applicable to the ESX host.  See also *HostPatchManagerReason_enum*.  | [optional] 
**integrity** | **str** | The integrity status of the update&#39;s metadata.  The value would be unset if the integrity status is unknown to the server.  See also *HostPatchManagerIntegrityStatus_enum*.  | [optional] 
**installed** | **bool** | Whether the update is installed on the server.  | 
**install_state** | **List[str]** | The installation state of the update.  Unset if the update is not installed on the server.  See also *HostPatchManagerInstallState_enum*.  | [optional] 
**prerequisite_patch** | [**List[HostPatchManagerStatusPrerequisitePatch]**](HostPatchManagerStatusPrerequisitePatch.md) | Prerequisite update.  | [optional] 
**restart_required** | **bool** | Whether or not this update requires a host restart to take effect.  | 
**reconnect_required** | **bool** | Whether or not this update requires caller to reconnect to the host.  This is usually because the update is on the agent that running on the host, the agent would thus be restarted when the update is applied. Caller can reconnect (and possibly relogin) to the host after the agent has been restarted.  | 
**vm_off_required** | **bool** | Whether or not this update requires the host in maintenance mode.  | 
**superseded_patch_ids** | **List[str]** | Patches that are superseded by this update.  | [optional] 

## Example

```python
from vmware_vi.models.host_patch_manager_status import HostPatchManagerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of HostPatchManagerStatus from a JSON string
host_patch_manager_status_instance = HostPatchManagerStatus.from_json(json)
# print the JSON string representation of the object
print HostPatchManagerStatus.to_json()

# convert the object into a dict
host_patch_manager_status_dict = host_patch_manager_status_instance.to_dict()
# create an instance of HostPatchManagerStatus from a dict
host_patch_manager_status_form_dict = host_patch_manager_status.from_dict(host_patch_manager_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


