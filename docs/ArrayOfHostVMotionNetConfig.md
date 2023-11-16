# ArrayOfHostVMotionNetConfig

A boxed array of *HostVMotionNetConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVMotionNetConfig]**](HostVMotionNetConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_v_motion_net_config import ArrayOfHostVMotionNetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVMotionNetConfig from a JSON string
array_of_host_v_motion_net_config_instance = ArrayOfHostVMotionNetConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVMotionNetConfig.to_json()

# convert the object into a dict
array_of_host_v_motion_net_config_dict = array_of_host_v_motion_net_config_instance.to_dict()
# create an instance of ArrayOfHostVMotionNetConfig from a dict
array_of_host_v_motion_net_config_form_dict = array_of_host_v_motion_net_config.from_dict(array_of_host_v_motion_net_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


