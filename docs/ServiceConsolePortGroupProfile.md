# ServiceConsolePortGroupProfile

The *ServiceConsolePortGroupProfile* data object represents the profile for a port group that will be used by the service console.  If a profile plug-in defines policies or subprofiles, use the *ApplyProfile.policy* or *ApplyProfile.property* list to access the additional configuration data.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_config** | [**IpAddressProfile**](IpAddressProfile.md) |  | 

## Example

```python
from vmware_vi.models.service_console_port_group_profile import ServiceConsolePortGroupProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConsolePortGroupProfile from a JSON string
service_console_port_group_profile_instance = ServiceConsolePortGroupProfile.from_json(json)
# print the JSON string representation of the object
print ServiceConsolePortGroupProfile.to_json()

# convert the object into a dict
service_console_port_group_profile_dict = service_console_port_group_profile_instance.to_dict()
# create an instance of ServiceConsolePortGroupProfile from a dict
service_console_port_group_profile_form_dict = service_console_port_group_profile.from_dict(service_console_port_group_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


