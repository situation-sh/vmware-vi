# HostUnresolvedVmfsResolutionResult

When an UnresolvedVmfsVolume has been resignatured or forceMounted, we want to return the original spec information along with newly created VMFS volume.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostUnresolvedVmfsResolutionSpec**](HostUnresolvedVmfsResolutionSpec.md) |  | 
**vmfs** | [**HostVmfsVolume**](HostVmfsVolume.md) |  | [optional] 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_unresolved_vmfs_resolution_result import HostUnresolvedVmfsResolutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostUnresolvedVmfsResolutionResult from a JSON string
host_unresolved_vmfs_resolution_result_instance = HostUnresolvedVmfsResolutionResult.from_json(json)
# print the JSON string representation of the object
print HostUnresolvedVmfsResolutionResult.to_json()

# convert the object into a dict
host_unresolved_vmfs_resolution_result_dict = host_unresolved_vmfs_resolution_result_instance.to_dict()
# create an instance of HostUnresolvedVmfsResolutionResult from a dict
host_unresolved_vmfs_resolution_result_form_dict = host_unresolved_vmfs_resolution_result.from_dict(host_unresolved_vmfs_resolution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


