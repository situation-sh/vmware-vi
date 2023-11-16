# ArrayOfDvsProfile

A boxed array of *DvsProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsProfile]**](DvsProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_profile import ArrayOfDvsProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsProfile from a JSON string
array_of_dvs_profile_instance = ArrayOfDvsProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsProfile.to_json()

# convert the object into a dict
array_of_dvs_profile_dict = array_of_dvs_profile_instance.to_dict()
# create an instance of ArrayOfDvsProfile from a dict
array_of_dvs_profile_form_dict = array_of_dvs_profile.from_dict(array_of_dvs_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


