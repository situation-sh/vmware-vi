# ArrayOfHostNasVolumeConfig

A boxed array of *HostNasVolumeConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNasVolumeConfig]**](HostNasVolumeConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nas_volume_config import ArrayOfHostNasVolumeConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNasVolumeConfig from a JSON string
array_of_host_nas_volume_config_instance = ArrayOfHostNasVolumeConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNasVolumeConfig.to_json()

# convert the object into a dict
array_of_host_nas_volume_config_dict = array_of_host_nas_volume_config_instance.to_dict()
# create an instance of ArrayOfHostNasVolumeConfig from a dict
array_of_host_nas_volume_config_form_dict = array_of_host_nas_volume_config.from_dict(array_of_host_nas_volume_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


