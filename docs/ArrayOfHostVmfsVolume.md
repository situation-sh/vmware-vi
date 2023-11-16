# ArrayOfHostVmfsVolume

A boxed array of *HostVmfsVolume*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVmfsVolume]**](HostVmfsVolume.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_vmfs_volume import ArrayOfHostVmfsVolume

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVmfsVolume from a JSON string
array_of_host_vmfs_volume_instance = ArrayOfHostVmfsVolume.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVmfsVolume.to_json()

# convert the object into a dict
array_of_host_vmfs_volume_dict = array_of_host_vmfs_volume_instance.to_dict()
# create an instance of ArrayOfHostVmfsVolume from a dict
array_of_host_vmfs_volume_form_dict = array_of_host_vmfs_volume.from_dict(array_of_host_vmfs_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


