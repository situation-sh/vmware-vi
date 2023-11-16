# ArrayOfHostNasVolume

A boxed array of *HostNasVolume*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNasVolume]**](HostNasVolume.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nas_volume import ArrayOfHostNasVolume

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNasVolume from a JSON string
array_of_host_nas_volume_instance = ArrayOfHostNasVolume.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNasVolume.to_json()

# convert the object into a dict
array_of_host_nas_volume_dict = array_of_host_nas_volume_instance.to_dict()
# create an instance of ArrayOfHostNasVolume from a dict
array_of_host_nas_volume_form_dict = array_of_host_nas_volume.from_dict(array_of_host_nas_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


