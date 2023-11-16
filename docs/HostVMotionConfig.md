# HostVMotionConfig

This data object configuring VMotion on the host.  The runtime information is available from the *VMotionInfo* data object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vmotion_nic_key** | **str** | Key of the VirtualNic used for VMotion.  | [optional] 
**enabled** | **bool** | Flag to indicate whether or not VMotion is enabled.  | 

## Example

```python
from vmware_vi.models.host_v_motion_config import HostVMotionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostVMotionConfig from a JSON string
host_v_motion_config_instance = HostVMotionConfig.from_json(json)
# print the JSON string representation of the object
print HostVMotionConfig.to_json()

# convert the object into a dict
host_v_motion_config_dict = host_v_motion_config_instance.to_dict()
# create an instance of HostVMotionConfig from a dict
host_v_motion_config_form_dict = host_v_motion_config.from_dict(host_v_motion_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


