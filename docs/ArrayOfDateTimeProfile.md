# ArrayOfDateTimeProfile

A boxed array of *DateTimeProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DateTimeProfile]**](DateTimeProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_date_time_profile import ArrayOfDateTimeProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDateTimeProfile from a JSON string
array_of_date_time_profile_instance = ArrayOfDateTimeProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfDateTimeProfile.to_json()

# convert the object into a dict
array_of_date_time_profile_dict = array_of_date_time_profile_instance.to_dict()
# create an instance of ArrayOfDateTimeProfile from a dict
array_of_date_time_profile_form_dict = array_of_date_time_profile.from_dict(array_of_date_time_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


