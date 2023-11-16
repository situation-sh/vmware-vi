# CheckHostPatchRequestType

The parameters of *HostPatchManager.CheckHostPatch_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_urls** | **List[str]** | a list of urls pointing to metadata.zip.  | [optional] 
**bundle_urls** | **List[str]** | a list of urls pointing to an \&quot;offline\&quot; bundle. It is not supported in 5.0 or later.  | [optional] 
**spec** | [**HostPatchManagerPatchManagerOperationSpec**](HostPatchManagerPatchManagerOperationSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.check_host_patch_request_type import CheckHostPatchRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CheckHostPatchRequestType from a JSON string
check_host_patch_request_type_instance = CheckHostPatchRequestType.from_json(json)
# print the JSON string representation of the object
print CheckHostPatchRequestType.to_json()

# convert the object into a dict
check_host_patch_request_type_dict = check_host_patch_request_type_instance.to_dict()
# create an instance of CheckHostPatchRequestType from a dict
check_host_patch_request_type_form_dict = check_host_patch_request_type.from_dict(check_host_patch_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


