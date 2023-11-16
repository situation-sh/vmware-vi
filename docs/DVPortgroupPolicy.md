# DVPortgroupPolicy

The DistributedVirtualPortgroup policies.  This field is not applicable when queried directly against an ESX host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_override_allowed** | **bool** | Allow the *DVPortSetting.blocked* setting of an individual port to override the setting in *DVPortgroupConfigInfo.defaultPortConfig* of a portgroup.  ***Since:*** vSphere API 4.0  | 
**shaping_override_allowed** | **bool** | Allow the *DVPortSetting.inShapingPolicy* or *DVPortSetting.outShapingPolicy* settings of an individual port to override the setting in *DVPortgroupConfigInfo.defaultPortConfig* of a portgroup.  ***Since:*** vSphere API 4.0  | 
**vendor_config_override_allowed** | **bool** | Allow the *DVPortSetting.vendorSpecificConfig* setting of an individual port to override the setting in *DVPortgroupConfigInfo.defaultPortConfig* of a portgroup.  ***Since:*** vSphere API 4.0  | 
**live_port_moving_allowed** | **bool** | Allow a live port to be moved in and out of the portgroup.  ***Since:*** vSphere API 4.0  | 
**port_config_reset_at_disconnect** | **bool** | If true, reset the port network setting back to the portgroup setting (thus removing the per-port setting) when the port is disconnected from the connectee.  ***Since:*** vSphere API 4.0  | 
**network_resource_pool_override_allowed** | **bool** | Allow the setting of *DVPortSetting.networkResourcePoolKey* of an individual port to override the setting in *DVPortgroupConfigInfo.defaultPortConfig* of a portgroup.  ***Since:*** vSphere API 5.0  | [optional] 
**traffic_filter_override_allowed** | **bool** | Allow the setting of *DVPortSetting.filterPolicy*, for an individual port to override the setting in *DVPortgroupConfigInfo.defaultPortConfig* of a portgroup.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.dv_portgroup_policy import DVPortgroupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortgroupPolicy from a JSON string
dv_portgroup_policy_instance = DVPortgroupPolicy.from_json(json)
# print the JSON string representation of the object
print DVPortgroupPolicy.to_json()

# convert the object into a dict
dv_portgroup_policy_dict = dv_portgroup_policy_instance.to_dict()
# create an instance of DVPortgroupPolicy from a dict
dv_portgroup_policy_form_dict = dv_portgroup_policy.from_dict(dv_portgroup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


