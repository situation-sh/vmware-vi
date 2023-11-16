# InstallHostPatchRequestType

The parameters of *HostPatchManager.InstallHostPatch_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | [**HostPatchManagerLocator**](HostPatchManagerLocator.md) |  | 
**update_id** | **str** | The update to be installed on the host.  | 
**force** | **bool** | Specify whether to force reinstall an update. By default, installing an already-installed update would fail with the *PatchAlreadyInstalled* fault. If force is set to true, the update will be forcefully reinstalled, thus overwriting the already installed update.  | [optional] 

## Example

```python
from vmware_vi.models.install_host_patch_request_type import InstallHostPatchRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of InstallHostPatchRequestType from a JSON string
install_host_patch_request_type_instance = InstallHostPatchRequestType.from_json(json)
# print the JSON string representation of the object
print InstallHostPatchRequestType.to_json()

# convert the object into a dict
install_host_patch_request_type_dict = install_host_patch_request_type_instance.to_dict()
# create an instance of InstallHostPatchRequestType from a dict
install_host_patch_request_type_form_dict = install_host_patch_request_type.from_dict(install_host_patch_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


