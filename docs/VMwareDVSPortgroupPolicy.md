# VMwareDVSPortgroupPolicy

This class defines the VMware specific configuration for DistributedVirtualPort.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_override_allowed** | **bool** | Allow the setting of *VmwareDistributedVirtualSwitchVlanIdSpec.vlanId*, trunk *VmwareDistributedVirtualSwitchTrunkVlanSpec.vlanId*, or *VmwareDistributedVirtualSwitchPvlanSpec.pvlanId* for an individual port to override the setting in *DVPortgroupConfigInfo.defaultPortConfig* of a portgroup.  ***Since:*** vSphere API 4.0  | 
**uplink_teaming_override_allowed** | **bool** | Allow the setting of *VMwareDVSPortSetting.uplinkTeamingPolicy* for an individual port to override the setting in *DVPortgroupConfigInfo.defaultPortConfig* of a portgroup.  ***Since:*** vSphere API 4.0  | 
**security_policy_override_allowed** | **bool** | Deprecated as of vSphere API 6.7.1, use *VMwareDVSPortgroupPolicy.macManagementOverrideAllowed* instead.  Allow the setting of *VMwareDVSPortSetting.securityPolicy* for an individual port to override the setting in *DVPortgroupConfigInfo.defaultPortConfig* of a portgroup.  ***Since:*** vSphere API 4.0  | 
**ipfix_override_allowed** | **bool** | Allow the setting of *VMwareDVSPortSetting.ipfixEnabled* for an individual port to override the setting in *DVPortgroupConfigInfo.defaultPortConfig* of a portgroup.  ***Since:*** vSphere API 5.0  | [optional] 
**mac_management_override_allowed** | **bool** | Allow the setting of *VMwareDVSPortSetting.macManagementPolicy* for an individual port to override the setting in *DVPortgroupConfigInfo.defaultPortConfig* of a portgroup.  ***Since:*** vSphere API 6.7.1  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_dvs_portgroup_policy import VMwareDVSPortgroupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSPortgroupPolicy from a JSON string
v_mware_dvs_portgroup_policy_instance = VMwareDVSPortgroupPolicy.from_json(json)
# print the JSON string representation of the object
print VMwareDVSPortgroupPolicy.to_json()

# convert the object into a dict
v_mware_dvs_portgroup_policy_dict = v_mware_dvs_portgroup_policy_instance.to_dict()
# create an instance of VMwareDVSPortgroupPolicy from a dict
v_mware_dvs_portgroup_policy_form_dict = v_mware_dvs_portgroup_policy.from_dict(v_mware_dvs_portgroup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


