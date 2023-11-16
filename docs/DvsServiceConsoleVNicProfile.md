# DvsServiceConsoleVNicProfile

The *DvsServiceConsoleVNicProfile* data object describes the IP configuration for a service console Virtual NIC connected to a distributed virtual switch.  The *DvsVNicProfile.ipConfig* property contains the Virtual NIC IP address. If a profile plug-in defines policies or subprofiles, use the *ApplyProfile.policy* or *ApplyProfile.property* list to access the additional configuration data.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dvs_service_console_v_nic_profile import DvsServiceConsoleVNicProfile

# TODO update the JSON string below
json = "{}"
# create an instance of DvsServiceConsoleVNicProfile from a JSON string
dvs_service_console_v_nic_profile_instance = DvsServiceConsoleVNicProfile.from_json(json)
# print the JSON string representation of the object
print DvsServiceConsoleVNicProfile.to_json()

# convert the object into a dict
dvs_service_console_v_nic_profile_dict = dvs_service_console_v_nic_profile_instance.to_dict()
# create an instance of DvsServiceConsoleVNicProfile from a dict
dvs_service_console_v_nic_profile_form_dict = dvs_service_console_v_nic_profile.from_dict(dvs_service_console_v_nic_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


