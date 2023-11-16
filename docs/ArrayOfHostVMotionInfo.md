# ArrayOfHostVMotionInfo

A boxed array of *HostVMotionInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostVMotionInfo]**](HostVMotionInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_v_motion_info import ArrayOfHostVMotionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostVMotionInfo from a JSON string
array_of_host_v_motion_info_instance = ArrayOfHostVMotionInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostVMotionInfo.to_json()

# convert the object into a dict
array_of_host_v_motion_info_dict = array_of_host_v_motion_info_instance.to_dict()
# create an instance of ArrayOfHostVMotionInfo from a dict
array_of_host_v_motion_info_form_dict = array_of_host_v_motion_info.from_dict(array_of_host_v_motion_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


