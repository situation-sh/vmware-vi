# VMwareUplinkPortOrderPolicy

This data object type describes uplink port ordering policy for a distributed virtual port.  A uplink port can be in the active list, the standby list, or neither. It cannot be in both lists.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_uplink_port** | **List[str]** | List of active uplink ports used for load balancing.  ***Since:*** vSphere API 4.0  | [optional] 
**standby_uplink_port** | **List[str]** | Standby uplink ports used for failover.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_uplink_port_order_policy import VMwareUplinkPortOrderPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareUplinkPortOrderPolicy from a JSON string
v_mware_uplink_port_order_policy_instance = VMwareUplinkPortOrderPolicy.from_json(json)
# print the JSON string representation of the object
print VMwareUplinkPortOrderPolicy.to_json()

# convert the object into a dict
v_mware_uplink_port_order_policy_dict = v_mware_uplink_port_order_policy_instance.to_dict()
# create an instance of VMwareUplinkPortOrderPolicy from a dict
v_mware_uplink_port_order_policy_form_dict = v_mware_uplink_port_order_policy.from_dict(v_mware_uplink_port_order_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


