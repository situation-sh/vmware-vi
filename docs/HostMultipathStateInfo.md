# HostMultipathStateInfo

This data object type describes the state of storage paths on the host.  All storage paths on the host are enumerated in this data object.  The reason all path state information is encapsulated in this data object is because the path may actively change. This data object ensures that a request to gather path state changes only needs to fetch this data object.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | [**List[HostMultipathStateInfoPath]**](HostMultipathStateInfoPath.md) | List of paths on the system and their path states.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_multipath_state_info import HostMultipathStateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostMultipathStateInfo from a JSON string
host_multipath_state_info_instance = HostMultipathStateInfo.from_json(json)
# print the JSON string representation of the object
print HostMultipathStateInfo.to_json()

# convert the object into a dict
host_multipath_state_info_dict = host_multipath_state_info_instance.to_dict()
# create an instance of HostMultipathStateInfo from a dict
host_multipath_state_info_form_dict = host_multipath_state_info.from_dict(host_multipath_state_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


