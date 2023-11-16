# StaticRouteProfile

The *StaticRouteProfile* data object represents a single static IP route.  The *ApplyProfile.policy* property contains data values for static route configuration.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.static_route_profile import StaticRouteProfile

# TODO update the JSON string below
json = "{}"
# create an instance of StaticRouteProfile from a JSON string
static_route_profile_instance = StaticRouteProfile.from_json(json)
# print the JSON string representation of the object
print StaticRouteProfile.to_json()

# convert the object into a dict
static_route_profile_dict = static_route_profile_instance.to_dict()
# create an instance of StaticRouteProfile from a dict
static_route_profile_form_dict = static_route_profile.from_dict(static_route_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


