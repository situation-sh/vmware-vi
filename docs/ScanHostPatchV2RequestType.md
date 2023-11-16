# ScanHostPatchV2RequestType

The parameters of *HostPatchManager.ScanHostPatchV2_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_urls** | **List[str]** | a list of urls pointing to metadata.zip.  | [optional] 
**bundle_urls** | **List[str]** | a list of urls pointing to an \&quot;offline\&quot; bundle. It is not supported in 5.0 or later.  | [optional] 
**spec** | [**HostPatchManagerPatchManagerOperationSpec**](HostPatchManagerPatchManagerOperationSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.scan_host_patch_v2_request_type import ScanHostPatchV2RequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ScanHostPatchV2RequestType from a JSON string
scan_host_patch_v2_request_type_instance = ScanHostPatchV2RequestType.from_json(json)
# print the JSON string representation of the object
print ScanHostPatchV2RequestType.to_json()

# convert the object into a dict
scan_host_patch_v2_request_type_dict = scan_host_patch_v2_request_type_instance.to_dict()
# create an instance of ScanHostPatchV2RequestType from a dict
scan_host_patch_v2_request_type_form_dict = scan_host_patch_v2_request_type.from_dict(scan_host_patch_v2_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


