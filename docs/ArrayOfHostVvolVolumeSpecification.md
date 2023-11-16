# ArrayOfHostVvolVolumeSpecification

A boxed array of *HostVvolVolumeSpecification*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVvolVolumeSpecification]**](HostVvolVolumeSpecification.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_vvol_volume_specification import ArrayOfHostVvolVolumeSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVvolVolumeSpecification from a JSON string
array_of_host_vvol_volume_specification_instance = ArrayOfHostVvolVolumeSpecification.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVvolVolumeSpecification.to_json()

# convert the object into a dict
array_of_host_vvol_volume_specification_dict = array_of_host_vvol_volume_specification_instance.to_dict()
# create an instance of ArrayOfHostVvolVolumeSpecification from a dict
array_of_host_vvol_volume_specification_form_dict = array_of_host_vvol_volume_specification.from_dict(array_of_host_vvol_volume_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


