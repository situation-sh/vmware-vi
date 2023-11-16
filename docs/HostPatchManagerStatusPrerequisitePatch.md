# HostPatchManagerStatusPrerequisitePatch

Updates that are required to be installed before this update can be installed on the server.  In addition to being installed on the server, an update can have additional requirement on the server or services running on the server pertaining to the prerequisite update. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the prerequisite update.  | 
**install_state** | **List[str]** | The requirement on the server or services running on the server pertaining to the prerequisite update.  For example, this update could require the server to be rebooted after the prerequisite update is installed. Unset if there is no additional requirement on the prerequisite update.  See also *HostPatchManagerInstallState_enum*.  | [optional] 

## Example

```python
from vmware_vi.models.host_patch_manager_status_prerequisite_patch import HostPatchManagerStatusPrerequisitePatch

# TODO update the JSON string below
json = "{}"
# create an instance of HostPatchManagerStatusPrerequisitePatch from a JSON string
host_patch_manager_status_prerequisite_patch_instance = HostPatchManagerStatusPrerequisitePatch.from_json(json)
# print the JSON string representation of the object
print HostPatchManagerStatusPrerequisitePatch.to_json()

# convert the object into a dict
host_patch_manager_status_prerequisite_patch_dict = host_patch_manager_status_prerequisite_patch_instance.to_dict()
# create an instance of HostPatchManagerStatusPrerequisitePatch from a dict
host_patch_manager_status_prerequisite_patch_form_dict = host_patch_manager_status_prerequisite_patch.from_dict(host_patch_manager_status_prerequisite_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


