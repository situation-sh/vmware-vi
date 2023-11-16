# HostVMotionInfo

Deprecated as of VI API 4.0, use *HostVirtualNicManagerInfo*.  This data object type describes VMotion host configuration data objects. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**net_config** | [**HostVMotionNetConfig**](HostVMotionNetConfig.md) |  | [optional] 
**ip_config** | [**HostIpConfig**](HostIpConfig.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_v_motion_info import HostVMotionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostVMotionInfo from a JSON string
host_v_motion_info_instance = HostVMotionInfo.from_json(json)
# print the JSON string representation of the object
print HostVMotionInfo.to_json()

# convert the object into a dict
host_v_motion_info_dict = host_v_motion_info_instance.to_dict()
# create an instance of HostVMotionInfo from a dict
host_v_motion_info_form_dict = host_v_motion_info.from_dict(host_v_motion_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


