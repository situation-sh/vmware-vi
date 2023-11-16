# NetStackInstanceProfile

The *NetStackInstanceProfile* data object represents a subprofile for a netStackInstance.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 5.5  | 
**dns_config** | [**NetworkProfileDnsConfigProfile**](NetworkProfileDnsConfigProfile.md) |  | 
**ip_route_config** | [**IpRouteProfile**](IpRouteProfile.md) |  | 

## Example

```python
from vmware_vi.models.net_stack_instance_profile import NetStackInstanceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of NetStackInstanceProfile from a JSON string
net_stack_instance_profile_instance = NetStackInstanceProfile.from_json(json)
# print the JSON string representation of the object
print NetStackInstanceProfile.to_json()

# convert the object into a dict
net_stack_instance_profile_dict = net_stack_instance_profile_instance.to_dict()
# create an instance of NetStackInstanceProfile from a dict
net_stack_instance_profile_form_dict = net_stack_instance_profile.from_dict(net_stack_instance_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


