# ArrayOfHostVmfsRescanResult

A boxed array of *HostVmfsRescanResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVmfsRescanResult]**](HostVmfsRescanResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_vmfs_rescan_result import ArrayOfHostVmfsRescanResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVmfsRescanResult from a JSON string
array_of_host_vmfs_rescan_result_instance = ArrayOfHostVmfsRescanResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVmfsRescanResult.to_json()

# convert the object into a dict
array_of_host_vmfs_rescan_result_dict = array_of_host_vmfs_rescan_result_instance.to_dict()
# create an instance of ArrayOfHostVmfsRescanResult from a dict
array_of_host_vmfs_rescan_result_form_dict = array_of_host_vmfs_rescan_result.from_dict(array_of_host_vmfs_rescan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


