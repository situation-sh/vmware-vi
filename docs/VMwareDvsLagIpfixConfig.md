# VMwareDvsLagIpfixConfig

This class defines the ipfix configuration of the Link Aggregation Control Protocol group.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipfix_enabled** | **bool** | True if ipfix monitoring is enabled in the Link Aggregation Control Protocol group.  If set, this property will override the ipfix configuration of Uplink Ports in the Link Aggregation Control Protocol group. Thus they are no longer inheriting ipfix configuration from their Uplink Port Group. Setting this property would require *VMwareDVSPortgroupPolicy.ipfixOverrideAllowed* of all the Uplink Port Groups to be true, otherwise ConflictingConfiguration fault will be raised.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_dvs_lag_ipfix_config import VMwareDvsLagIpfixConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDvsLagIpfixConfig from a JSON string
v_mware_dvs_lag_ipfix_config_instance = VMwareDvsLagIpfixConfig.from_json(json)
# print the JSON string representation of the object
print VMwareDvsLagIpfixConfig.to_json()

# convert the object into a dict
v_mware_dvs_lag_ipfix_config_dict = v_mware_dvs_lag_ipfix_config_instance.to_dict()
# create an instance of VMwareDvsLagIpfixConfig from a dict
v_mware_dvs_lag_ipfix_config_form_dict = v_mware_dvs_lag_ipfix_config.from_dict(v_mware_dvs_lag_ipfix_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


