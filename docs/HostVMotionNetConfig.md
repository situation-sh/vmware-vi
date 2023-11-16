# HostVMotionNetConfig

The NetConfig data object type contains the networking configuration for VMotion operations. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_vnic** | [**List[HostVirtualNic]**](HostVirtualNic.md) | List of VirtualNic objects that may be used for VMotion.  This will be a subset of the list of VirtualNics in *HostNetworkInfo.vnic*.  | [optional] 
**selected_vnic** | [**HostVirtualNic**](HostVirtualNic.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_v_motion_net_config import HostVMotionNetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostVMotionNetConfig from a JSON string
host_v_motion_net_config_instance = HostVMotionNetConfig.from_json(json)
# print the JSON string representation of the object
print HostVMotionNetConfig.to_json()

# convert the object into a dict
host_v_motion_net_config_dict = host_v_motion_net_config_instance.to_dict()
# create an instance of HostVMotionNetConfig from a dict
host_v_motion_net_config_form_dict = host_v_motion_net_config.from_dict(host_v_motion_net_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


