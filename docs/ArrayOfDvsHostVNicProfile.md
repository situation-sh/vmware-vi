# ArrayOfDvsHostVNicProfile

A boxed array of *DvsHostVNicProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsHostVNicProfile]**](DvsHostVNicProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_host_v_nic_profile import ArrayOfDvsHostVNicProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsHostVNicProfile from a JSON string
array_of_dvs_host_v_nic_profile_instance = ArrayOfDvsHostVNicProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsHostVNicProfile.to_json()

# convert the object into a dict
array_of_dvs_host_v_nic_profile_dict = array_of_dvs_host_v_nic_profile_instance.to_dict()
# create an instance of ArrayOfDvsHostVNicProfile from a dict
array_of_dvs_host_v_nic_profile_form_dict = array_of_dvs_host_v_nic_profile.from_dict(array_of_dvs_host_v_nic_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


