# HostPortGroupProfile

The *HostPortGroupProfile* data object represents the subprofile for a port group that will be used by the ESX host.  If a profile plug-in defines policies or subprofiles, use the *ApplyProfile.policy* or *ApplyProfile.property* list to access the additional configuration data.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_config** | [**IpAddressProfile**](IpAddressProfile.md) |  | 

## Example

```python
from vmware_vi.models.host_port_group_profile import HostPortGroupProfile

# TODO update the JSON string below
json = "{}"
# create an instance of HostPortGroupProfile from a JSON string
host_port_group_profile_instance = HostPortGroupProfile.from_json(json)
# print the JSON string representation of the object
print HostPortGroupProfile.to_json()

# convert the object into a dict
host_port_group_profile_dict = host_port_group_profile_instance.to_dict()
# create an instance of HostPortGroupProfile from a dict
host_port_group_profile_form_dict = host_port_group_profile.from_dict(host_port_group_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


