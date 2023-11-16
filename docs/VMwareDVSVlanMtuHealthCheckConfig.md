# VMwareDVSVlanMtuHealthCheckConfig

This class defines the vlan and mtu health check configuration.  Vlan health check is used to check whether vlans are trunked by the physical switch connected to the uplink ports. MTU health check is used to verify current MTU setting workable on all uplink ports of the vSphere Distributed Switch.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.v_mware_dvs_vlan_mtu_health_check_config import VMwareDVSVlanMtuHealthCheckConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSVlanMtuHealthCheckConfig from a JSON string
v_mware_dvs_vlan_mtu_health_check_config_instance = VMwareDVSVlanMtuHealthCheckConfig.from_json(json)
# print the JSON string representation of the object
print VMwareDVSVlanMtuHealthCheckConfig.to_json()

# convert the object into a dict
v_mware_dvs_vlan_mtu_health_check_config_dict = v_mware_dvs_vlan_mtu_health_check_config_instance.to_dict()
# create an instance of VMwareDVSVlanMtuHealthCheckConfig from a dict
v_mware_dvs_vlan_mtu_health_check_config_form_dict = v_mware_dvs_vlan_mtu_health_check_config.from_dict(v_mware_dvs_vlan_mtu_health_check_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


