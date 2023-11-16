# ArrayOfStaticRouteProfile

A boxed array of *StaticRouteProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StaticRouteProfile]**](StaticRouteProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_static_route_profile import ArrayOfStaticRouteProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStaticRouteProfile from a JSON string
array_of_static_route_profile_instance = ArrayOfStaticRouteProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfStaticRouteProfile.to_json()

# convert the object into a dict
array_of_static_route_profile_dict = array_of_static_route_profile_instance.to_dict()
# create an instance of ArrayOfStaticRouteProfile from a dict
array_of_static_route_profile_form_dict = array_of_static_route_profile.from_dict(array_of_static_route_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


