# ArrayOfHostUnresolvedVmfsVolume

A boxed array of *HostUnresolvedVmfsVolume*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostUnresolvedVmfsVolume]**](HostUnresolvedVmfsVolume.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_unresolved_vmfs_volume import ArrayOfHostUnresolvedVmfsVolume

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostUnresolvedVmfsVolume from a JSON string
array_of_host_unresolved_vmfs_volume_instance = ArrayOfHostUnresolvedVmfsVolume.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostUnresolvedVmfsVolume.to_json()

# convert the object into a dict
array_of_host_unresolved_vmfs_volume_dict = array_of_host_unresolved_vmfs_volume_instance.to_dict()
# create an instance of ArrayOfHostUnresolvedVmfsVolume from a dict
array_of_host_unresolved_vmfs_volume_form_dict = array_of_host_unresolved_vmfs_volume.from_dict(array_of_host_unresolved_vmfs_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


