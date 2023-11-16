# ArrayOfDvsVNicProfile

A boxed array of *DvsVNicProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsVNicProfile]**](DvsVNicProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_v_nic_profile import ArrayOfDvsVNicProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsVNicProfile from a JSON string
array_of_dvs_v_nic_profile_instance = ArrayOfDvsVNicProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsVNicProfile.to_json()

# convert the object into a dict
array_of_dvs_v_nic_profile_dict = array_of_dvs_v_nic_profile_instance.to_dict()
# create an instance of ArrayOfDvsVNicProfile from a dict
array_of_dvs_v_nic_profile_form_dict = array_of_dvs_v_nic_profile.from_dict(array_of_dvs_v_nic_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


