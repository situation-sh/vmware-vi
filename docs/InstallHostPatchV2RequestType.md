# InstallHostPatchV2RequestType

The parameters of *HostPatchManager.InstallHostPatchV2_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_urls** | **List[str]** | A list of urls pointing to metadata.zip.  | [optional] 
**bundle_urls** | **List[str]** | a list of urls pointing to an \&quot;offline\&quot; bundle. It is not supported in 5.0 or later.  | [optional] 
**vib_urls** | **List[str]** | The urls of update binary files to be installed.  | [optional] 
**spec** | [**HostPatchManagerPatchManagerOperationSpec**](HostPatchManagerPatchManagerOperationSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.install_host_patch_v2_request_type import InstallHostPatchV2RequestType

# TODO update the JSON string below
json = "{}"
# create an instance of InstallHostPatchV2RequestType from a JSON string
install_host_patch_v2_request_type_instance = InstallHostPatchV2RequestType.from_json(json)
# print the JSON string representation of the object
print InstallHostPatchV2RequestType.to_json()

# convert the object into a dict
install_host_patch_v2_request_type_dict = install_host_patch_v2_request_type_instance.to_dict()
# create an instance of InstallHostPatchV2RequestType from a dict
install_host_patch_v2_request_type_form_dict = install_host_patch_v2_request_type.from_dict(install_host_patch_v2_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


