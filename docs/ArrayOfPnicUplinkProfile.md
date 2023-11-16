# ArrayOfPnicUplinkProfile

A boxed array of *PnicUplinkProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PnicUplinkProfile]**](PnicUplinkProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_pnic_uplink_profile import ArrayOfPnicUplinkProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfPnicUplinkProfile from a JSON string
array_of_pnic_uplink_profile_instance = ArrayOfPnicUplinkProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfPnicUplinkProfile.to_json()

# convert the object into a dict
array_of_pnic_uplink_profile_dict = array_of_pnic_uplink_profile_instance.to_dict()
# create an instance of ArrayOfPnicUplinkProfile from a dict
array_of_pnic_uplink_profile_form_dict = array_of_pnic_uplink_profile.from_dict(array_of_pnic_uplink_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


