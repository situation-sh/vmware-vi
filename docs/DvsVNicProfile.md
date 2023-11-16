# DvsVNicProfile

The *DvsVNicProfile* data object is the base object for host and service console Virtual NIC subprofiles.  If a profile plug-in defines additional policies or subprofiles, use the *ApplyProfile.policy* or *ApplyProfile.property* list to access the configuration data.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 4.0  | 
**ip_config** | [**IpAddressProfile**](IpAddressProfile.md) |  | 

## Example

```python
from vmware_vi.models.dvs_v_nic_profile import DvsVNicProfile

# TODO update the JSON string below
json = "{}"
# create an instance of DvsVNicProfile from a JSON string
dvs_v_nic_profile_instance = DvsVNicProfile.from_json(json)
# print the JSON string representation of the object
print DvsVNicProfile.to_json()

# convert the object into a dict
dvs_v_nic_profile_dict = dvs_v_nic_profile_instance.to_dict()
# create an instance of DvsVNicProfile from a dict
dvs_v_nic_profile_form_dict = dvs_v_nic_profile.from_dict(dvs_v_nic_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


