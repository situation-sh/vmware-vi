# ArrayOfIpRouteProfile

A boxed array of *IpRouteProfile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IpRouteProfile]**](IpRouteProfile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ip_route_profile import ArrayOfIpRouteProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIpRouteProfile from a JSON string
array_of_ip_route_profile_instance = ArrayOfIpRouteProfile.from_json(json)
# print the JSON string representation of the object
print ArrayOfIpRouteProfile.to_json()

# convert the object into a dict
array_of_ip_route_profile_dict = array_of_ip_route_profile_instance.to_dict()
# create an instance of ArrayOfIpRouteProfile from a dict
array_of_ip_route_profile_form_dict = array_of_ip_route_profile.from_dict(array_of_ip_route_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


