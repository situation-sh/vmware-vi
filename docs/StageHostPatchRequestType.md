# StageHostPatchRequestType

The parameters of *HostPatchManager.StageHostPatch_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_urls** | **List[str]** | A list of urls pointing to metadata.zip.  | [optional] 
**bundle_urls** | **List[str]** | a list of urls pointing to an \&quot;offline\&quot; bundle. It is not supported in 5.0 or later.  | [optional] 
**vib_urls** | **List[str]** | The urls of update binary files to be staged.  | [optional] 
**spec** | [**HostPatchManagerPatchManagerOperationSpec**](HostPatchManagerPatchManagerOperationSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.stage_host_patch_request_type import StageHostPatchRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of StageHostPatchRequestType from a JSON string
stage_host_patch_request_type_instance = StageHostPatchRequestType.from_json(json)
# print the JSON string representation of the object
print StageHostPatchRequestType.to_json()

# convert the object into a dict
stage_host_patch_request_type_dict = stage_host_patch_request_type_instance.to_dict()
# create an instance of StageHostPatchRequestType from a dict
stage_host_patch_request_type_form_dict = stage_host_patch_request_type.from_dict(stage_host_patch_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


