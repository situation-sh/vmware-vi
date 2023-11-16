# VirtualSwitchProfile

The *VirtualSwitchProfile* data object represents a subprofile for a virtual switch.  If a profile plug-in defines policies or subprofiles, use the *ApplyProfile.policy* or *ApplyProfile.property* list to access the additional configuration data.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 4.0  | 
**name** | **str** | Name of the standard virtual switch(VSS).  ***Since:*** vSphere API 4.0  | 
**link** | [**LinkProfile**](LinkProfile.md) |  | 
**num_ports** | [**NumPortsProfile**](NumPortsProfile.md) |  | 
**network_policy** | [**NetworkPolicyProfile**](NetworkPolicyProfile.md) |  | 

## Example

```python
from vmware_vi.models.virtual_switch_profile import VirtualSwitchProfile

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSwitchProfile from a JSON string
virtual_switch_profile_instance = VirtualSwitchProfile.from_json(json)
# print the JSON string representation of the object
print VirtualSwitchProfile.to_json()

# convert the object into a dict
virtual_switch_profile_dict = virtual_switch_profile_instance.to_dict()
# create an instance of VirtualSwitchProfile from a dict
virtual_switch_profile_form_dict = virtual_switch_profile.from_dict(virtual_switch_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


