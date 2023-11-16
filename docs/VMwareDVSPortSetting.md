# VMwareDVSPortSetting

This class defines the VMware specific configuration for DistributedVirtualPort.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan** | [**VmwareDistributedVirtualSwitchVlanSpec**](VmwareDistributedVirtualSwitchVlanSpec.md) |  | [optional] 
**qos_tag** | [**IntPolicy**](IntPolicy.md) |  | [optional] 
**uplink_teaming_policy** | [**VmwareUplinkPortTeamingPolicy**](VmwareUplinkPortTeamingPolicy.md) |  | [optional] 
**security_policy** | [**DVSSecurityPolicy**](DVSSecurityPolicy.md) |  | [optional] 
**ipfix_enabled** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 
**tx_uplink** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 
**lacp_policy** | [**VMwareUplinkLacpPolicy**](VMwareUplinkLacpPolicy.md) |  | [optional] 
**mac_management_policy** | [**DVSMacManagementPolicy**](DVSMacManagementPolicy.md) |  | [optional] 
**vni** | [**IntPolicy**](IntPolicy.md) |  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_dvs_port_setting import VMwareDVSPortSetting

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSPortSetting from a JSON string
v_mware_dvs_port_setting_instance = VMwareDVSPortSetting.from_json(json)
# print the JSON string representation of the object
print VMwareDVSPortSetting.to_json()

# convert the object into a dict
v_mware_dvs_port_setting_dict = v_mware_dvs_port_setting_instance.to_dict()
# create an instance of VMwareDVSPortSetting from a dict
v_mware_dvs_port_setting_form_dict = v_mware_dvs_port_setting.from_dict(v_mware_dvs_port_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


