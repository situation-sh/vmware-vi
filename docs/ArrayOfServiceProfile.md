# ArrayOfServiceProfile

A boxed array of *ServiceProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ServiceProfile]**](ServiceProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_service_profile import ArrayOfServiceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfServiceProfile from a JSON string
array_of_service_profile_instance = ArrayOfServiceProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfServiceProfile.to_json()

# convert the object into a dict
array_of_service_profile_dict = array_of_service_profile_instance.to_dict()
# create an instance of ArrayOfServiceProfile from a dict
array_of_service_profile_form_dict = array_of_service_profile.from_dict(array_of_service_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


