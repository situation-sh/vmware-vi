# HostMultipathStateInfoPath

Data object indicating state of storage path for a named path.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of path.  Use this name to enable or disable storage paths *HostStorageSystem.EnableMultipathPath* and *HostStorageSystem.DisableMultipathPath*.  In addition to being the identifier for the path state operations, the name is used to correlate this object to the corresponding Path object in other contexts.  See also *HostPlugStoreTopologyPath.name*.  ***Since:*** vSphere API 4.0  | 
**path_state** | **str** | The state of the path.  Must be one of the values of *MultipathState_enum*.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.host_multipath_state_info_path import HostMultipathStateInfoPath

# TODO update the JSON string below
json = "{}"
# create an instance of HostMultipathStateInfoPath from a JSON string
host_multipath_state_info_path_instance = HostMultipathStateInfoPath.from_json(json)
# print the JSON string representation of the object
print HostMultipathStateInfoPath.to_json()

# convert the object into a dict
host_multipath_state_info_path_dict = host_multipath_state_info_path_instance.to_dict()
# create an instance of HostMultipathStateInfoPath from a dict
host_multipath_state_info_path_form_dict = host_multipath_state_info_path.from_dict(host_multipath_state_info_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


