# ArrayOfHostUnresolvedVmfsResolutionResult

A boxed array of *HostUnresolvedVmfsResolutionResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostUnresolvedVmfsResolutionResult]**](HostUnresolvedVmfsResolutionResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_unresolved_vmfs_resolution_result import ArrayOfHostUnresolvedVmfsResolutionResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostUnresolvedVmfsResolutionResult from a JSON string
array_of_host_unresolved_vmfs_resolution_result_instance = ArrayOfHostUnresolvedVmfsResolutionResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostUnresolvedVmfsResolutionResult.to_json()

# convert the object into a dict
array_of_host_unresolved_vmfs_resolution_result_dict = array_of_host_unresolved_vmfs_resolution_result_instance.to_dict()
# create an instance of ArrayOfHostUnresolvedVmfsResolutionResult from a dict
array_of_host_unresolved_vmfs_resolution_result_form_dict = array_of_host_unresolved_vmfs_resolution_result.from_dict(array_of_host_unresolved_vmfs_resolution_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


