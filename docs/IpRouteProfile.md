# IpRouteProfile

The *IpRouteProfile* data object represents the host IP route configuration.  If a profile plug-in defines policies or subprofiles, use the *ApplyProfile.policy* or *ApplyProfile.property* list to access the additional configuration data.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**static_route** | [**List[StaticRouteProfile]**](StaticRouteProfile.md) | List of static routes to be configured.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.ip_route_profile import IpRouteProfile

# TODO update the JSON string below
json = "{}"
# create an instance of IpRouteProfile from a JSON string
ip_route_profile_instance = IpRouteProfile.from_json(json)
# print the JSON string representation of the object
print IpRouteProfile.to_json()

# convert the object into a dict
ip_route_profile_dict = ip_route_profile_instance.to_dict()
# create an instance of IpRouteProfile from a dict
ip_route_profile_form_dict = ip_route_profile.from_dict(ip_route_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


