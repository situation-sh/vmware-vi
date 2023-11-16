# VMwareDvsLacpGroupConfig

This class defines VMware specific multiple IEEE 802.3ad Dynamic Link Aggregation Control Protocol groups.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The generated key as the identifier for the Link Aggregation group.  ***Since:*** vSphere API 5.5  | [optional] 
**name** | **str** | The display name.  ***Since:*** vSphere API 5.5  | [optional] 
**mode** | **str** | The mode of Link Aggregation Control Protocol.  See *VMwareUplinkLacpMode_enum* for valid values.  ***Since:*** vSphere API 5.5  | [optional] 
**uplink_num** | **int** | The number of uplink ports.  ***Since:*** vSphere API 5.5  | [optional] 
**loadbalance_algorithm** | **str** | Load balance policy.  See *VMwareDvsLacpLoadBalanceAlgorithm_enum* for valid values.  ***Since:*** vSphere API 5.5  | [optional] 
**vlan** | [**VMwareDvsLagVlanConfig**](VMwareDvsLagVlanConfig.md) |  | [optional] 
**ipfix** | [**VMwareDvsLagIpfixConfig**](VMwareDvsLagIpfixConfig.md) |  | [optional] 
**uplink_name** | **List[str]** | Names for the Uplink Ports in the group.  This property is ignored in an update operation.  ***Since:*** vSphere API 5.5  | [optional] 
**uplink_port_key** | **List[str]** | Keys for the Uplink Ports in the group.  This property is ignored in an update operation.  ***Since:*** vSphere API 5.5  | [optional] 
**timeout_mode** | **str** | The timeout mode of LACP group.  See *VMwareUplinkLacpTimeoutMode_enum* for valid values.  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_dvs_lacp_group_config import VMwareDvsLacpGroupConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDvsLacpGroupConfig from a JSON string
v_mware_dvs_lacp_group_config_instance = VMwareDvsLacpGroupConfig.from_json(json)
# print the JSON string representation of the object
print VMwareDvsLacpGroupConfig.to_json()

# convert the object into a dict
v_mware_dvs_lacp_group_config_dict = v_mware_dvs_lacp_group_config_instance.to_dict()
# create an instance of VMwareDvsLacpGroupConfig from a dict
v_mware_dvs_lacp_group_config_form_dict = v_mware_dvs_lacp_group_config.from_dict(v_mware_dvs_lacp_group_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


