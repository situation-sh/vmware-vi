# ScanHostPatchRequestType

The parameters of *HostPatchManager.ScanHostPatch_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | [**HostPatchManagerLocator**](HostPatchManagerLocator.md) |  | 
**update_id** | **List[str]** | The updates to scan. Wildcards can be used to specify the update IDs. The wildcards will be expanded to include all updates whose IDs match the specified wildcard and whose metadata is available in the repository. Specifying no update is equivalent to a wildcard \&quot;\\*\&quot;. In this case all updates available in the repository will be scanned.  | [optional] 

## Example

```python
from vmware_vi.models.scan_host_patch_request_type import ScanHostPatchRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ScanHostPatchRequestType from a JSON string
scan_host_patch_request_type_instance = ScanHostPatchRequestType.from_json(json)
# print the JSON string representation of the object
print ScanHostPatchRequestType.to_json()

# convert the object into a dict
scan_host_patch_request_type_dict = scan_host_patch_request_type_instance.to_dict()
# create an instance of ScanHostPatchRequestType from a dict
scan_host_patch_request_type_form_dict = scan_host_patch_request_type.from_dict(scan_host_patch_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


