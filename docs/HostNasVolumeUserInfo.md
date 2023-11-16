# HostNasVolumeUserInfo

NFS user authentication information  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | User name for authentication.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.host_nas_volume_user_info import HostNasVolumeUserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostNasVolumeUserInfo from a JSON string
host_nas_volume_user_info_instance = HostNasVolumeUserInfo.from_json(json)
# print the JSON string representation of the object
print HostNasVolumeUserInfo.to_json()

# convert the object into a dict
host_nas_volume_user_info_dict = host_nas_volume_user_info_instance.to_dict()
# create an instance of HostNasVolumeUserInfo from a dict
host_nas_volume_user_info_form_dict = host_nas_volume_user_info.from_dict(host_nas_volume_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


