# VMwareDvsLagVlanConfig

This class defines the vlan configuration of the Link Aggregation Control Protocol group.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_id** | [**List[NumericRange]**](NumericRange.md) | The VlanId range for the Uplink Ports in the Link Aggregation Control Protocol group.  The valid VlanId range is from 0 to 4094. Overlapping ranges are allowed. If set, this property will override the VLAN configuration of Uplink Ports in the Link Aggregation Control Protocol group. Thus they are no longer inheriting VLAN configuration from their Uplink Port Group. Setting this property would require *VMwareDVSPortgroupPolicy.vlanOverrideAllowed* of all the Uplink Port Groups to be true, otherwise ConflictingConfiguration fault will be raised.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_dvs_lag_vlan_config import VMwareDvsLagVlanConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDvsLagVlanConfig from a JSON string
v_mware_dvs_lag_vlan_config_instance = VMwareDvsLagVlanConfig.from_json(json)
# print the JSON string representation of the object
print VMwareDvsLagVlanConfig.to_json()

# convert the object into a dict
v_mware_dvs_lag_vlan_config_dict = v_mware_dvs_lag_vlan_config_instance.to_dict()
# create an instance of VMwareDvsLagVlanConfig from a dict
v_mware_dvs_lag_vlan_config_form_dict = v_mware_dvs_lag_vlan_config.from_dict(v_mware_dvs_lag_vlan_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


