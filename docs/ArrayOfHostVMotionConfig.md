# ArrayOfHostVMotionConfig

A boxed array of *HostVMotionConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVMotionConfig]**](HostVMotionConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_v_motion_config import ArrayOfHostVMotionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVMotionConfig from a JSON string
array_of_host_v_motion_config_instance = ArrayOfHostVMotionConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVMotionConfig.to_json()

# convert the object into a dict
array_of_host_v_motion_config_dict = array_of_host_v_motion_config_instance.to_dict()
# create an instance of ArrayOfHostVMotionConfig from a dict
array_of_host_v_motion_config_form_dict = array_of_host_v_motion_config.from_dict(array_of_host_v_motion_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


