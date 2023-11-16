# UninstallHostPatchRequestType

The parameters of *HostPatchManager.UninstallHostPatch_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulletin_ids** | **List[str]** | A list of bulletin IDs to be removed.  | [optional] 
**spec** | [**HostPatchManagerPatchManagerOperationSpec**](HostPatchManagerPatchManagerOperationSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.uninstall_host_patch_request_type import UninstallHostPatchRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UninstallHostPatchRequestType from a JSON string
uninstall_host_patch_request_type_instance = UninstallHostPatchRequestType.from_json(json)
# print the JSON string representation of the object
print UninstallHostPatchRequestType.to_json()

# convert the object into a dict
uninstall_host_patch_request_type_dict = uninstall_host_patch_request_type_instance.to_dict()
# create an instance of UninstallHostPatchRequestType from a dict
uninstall_host_patch_request_type_form_dict = uninstall_host_patch_request_type.from_dict(uninstall_host_patch_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


