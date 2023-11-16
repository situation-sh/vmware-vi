# DvsHostVNicProfile

The *DvsHostVNicProfile* data object describes the IP configuration for a host Virtual NIC connected to a distributed virtual switch.  The *DvsVNicProfile.ipConfig* property contains the Virtual NIC IP address. If a profile plug-in defines policies or subprofiles, use the *ApplyProfile.policy* or *ApplyProfile.property* list to access the additional configuration data.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dvs_host_v_nic_profile import DvsHostVNicProfile

# TODO update the JSON string below
json = "{}"
# create an instance of DvsHostVNicProfile from a JSON string
dvs_host_v_nic_profile_instance = DvsHostVNicProfile.from_json(json)
# print the JSON string representation of the object
print DvsHostVNicProfile.to_json()

# convert the object into a dict
dvs_host_v_nic_profile_dict = dvs_host_v_nic_profile_instance.to_dict()
# create an instance of DvsHostVNicProfile from a dict
dvs_host_v_nic_profile_form_dict = dvs_host_v_nic_profile.from_dict(dvs_host_v_nic_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


