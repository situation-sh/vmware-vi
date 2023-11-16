# ArrayOfNsxHostVNicProfile

A boxed array of *NsxHostVNicProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NsxHostVNicProfile]**](NsxHostVNicProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_nsx_host_v_nic_profile import ArrayOfNsxHostVNicProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNsxHostVNicProfile from a JSON string
array_of_nsx_host_v_nic_profile_instance = ArrayOfNsxHostVNicProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfNsxHostVNicProfile.to_json()

# convert the object into a dict
array_of_nsx_host_v_nic_profile_dict = array_of_nsx_host_v_nic_profile_instance.to_dict()
# create an instance of ArrayOfNsxHostVNicProfile from a dict
array_of_nsx_host_v_nic_profile_form_dict = array_of_nsx_host_v_nic_profile.from_dict(array_of_nsx_host_v_nic_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


