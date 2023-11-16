# ArrayOfHostVvolVolume

A boxed array of *HostVvolVolume*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVvolVolume]**](HostVvolVolume.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_vvol_volume import ArrayOfHostVvolVolume

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVvolVolume from a JSON string
array_of_host_vvol_volume_instance = ArrayOfHostVvolVolume.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVvolVolume.to_json()

# convert the object into a dict
array_of_host_vvol_volume_dict = array_of_host_vvol_volume_instance.to_dict()
# create an instance of ArrayOfHostVvolVolume from a dict
array_of_host_vvol_volume_form_dict = array_of_host_vvol_volume.from_dict(array_of_host_vvol_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


