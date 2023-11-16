# ArrayOfHostMultipathStateInfo

A boxed array of *HostMultipathStateInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostMultipathStateInfo]**](HostMultipathStateInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_multipath_state_info import ArrayOfHostMultipathStateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostMultipathStateInfo from a JSON string
array_of_host_multipath_state_info_instance = ArrayOfHostMultipathStateInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostMultipathStateInfo.to_json()

# convert the object into a dict
array_of_host_multipath_state_info_dict = array_of_host_multipath_state_info_instance.to_dict()
# create an instance of ArrayOfHostMultipathStateInfo from a dict
array_of_host_multipath_state_info_form_dict = array_of_host_multipath_state_info.from_dict(array_of_host_multipath_state_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


