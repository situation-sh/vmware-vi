# HostVmfsRescanResult

When a user resignatures an UnresolvedVmfsVolume through DatastoreSystem API, we resignature and auto-mount on the other hosts which share the same underlying storage luns.  As part of the operation, we rescan host. This data object describes the outcome of rescan operation on a host  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_vmfs_rescan_result import HostVmfsRescanResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostVmfsRescanResult from a JSON string
host_vmfs_rescan_result_instance = HostVmfsRescanResult.from_json(json)
# print the JSON string representation of the object
print HostVmfsRescanResult.to_json()

# convert the object into a dict
host_vmfs_rescan_result_dict = host_vmfs_rescan_result_instance.to_dict()
# create an instance of HostVmfsRescanResult from a dict
host_vmfs_rescan_result_form_dict = host_vmfs_rescan_result.from_dict(host_vmfs_rescan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


