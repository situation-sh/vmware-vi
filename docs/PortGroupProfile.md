# PortGroupProfile

*PortGroupProfile* is the base class for the different port group subprofile objects.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Linkable identifier.  ***Since:*** vSphere API 4.0  | 
**name** | **str** | Name of the portgroup.  ***Since:*** vSphere API 4.0  | 
**vlan** | [**VlanProfile**](VlanProfile.md) |  | 
**vswitch** | [**VirtualSwitchSelectionProfile**](VirtualSwitchSelectionProfile.md) |  | 
**network_policy** | [**NetworkPolicyProfile**](NetworkPolicyProfile.md) |  | 

## Example

```python
from vmware_vi.models.port_group_profile import PortGroupProfile

# TODO update the JSON string below
json = "{}"
# create an instance of PortGroupProfile from a JSON string
port_group_profile_instance = PortGroupProfile.from_json(json)
# print the JSON string representation of the object
print PortGroupProfile.to_json()

# convert the object into a dict
port_group_profile_dict = port_group_profile_instance.to_dict()
# create an instance of PortGroupProfile from a dict
port_group_profile_form_dict = port_group_profile.from_dict(port_group_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


