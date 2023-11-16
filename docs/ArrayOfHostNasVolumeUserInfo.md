# ArrayOfHostNasVolumeUserInfo

A boxed array of *HostNasVolumeUserInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNasVolumeUserInfo]**](HostNasVolumeUserInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_nas_volume_user_info import ArrayOfHostNasVolumeUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNasVolumeUserInfo from a JSON string
array_of_host_nas_volume_user_info_instance = ArrayOfHostNasVolumeUserInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNasVolumeUserInfo.to_json()

# convert the object into a dict
array_of_host_nas_volume_user_info_dict = array_of_host_nas_volume_user_info_instance.to_dict()
# create an instance of ArrayOfHostNasVolumeUserInfo from a dict
array_of_host_nas_volume_user_info_form_dict = array_of_host_nas_volume_user_info.from_dict(array_of_host_nas_volume_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


