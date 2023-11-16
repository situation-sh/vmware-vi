# NsxHostVNicProfile

The *NsxHostVNicProfile* data object is the base object for host Virtual NIC connected to NSX logic switch subprofiles.  If a profile plug-in defines additional policies or subprofiles, use the *ApplyProfile.policy* or *ApplyProfile.property* list to access the configuration data.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 6.7  | 
**ip_config** | [**IpAddressProfile**](IpAddressProfile.md) |  | 

## Example

```python
from vmware_vi.models.nsx_host_v_nic_profile import NsxHostVNicProfile

# TODO update the JSON string below
json = "{}"
# create an instance of NsxHostVNicProfile from a JSON string
nsx_host_v_nic_profile_instance = NsxHostVNicProfile.from_json(json)
# print the JSON string representation of the object
print NsxHostVNicProfile.to_json()

# convert the object into a dict
nsx_host_v_nic_profile_dict = nsx_host_v_nic_profile_instance.to_dict()
# create an instance of NsxHostVNicProfile from a dict
nsx_host_v_nic_profile_form_dict = nsx_host_v_nic_profile.from_dict(nsx_host_v_nic_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


