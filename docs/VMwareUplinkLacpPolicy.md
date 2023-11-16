# VMwareUplinkLacpPolicy

Deprecated as of vSphere API 5.5.  This class defines VMware specific Link Aggregation Control Protocol policy.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | [**BoolPolicy**](BoolPolicy.md) |  | [optional] 
**mode** | [**StringPolicy**](StringPolicy.md) |  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_uplink_lacp_policy import VMwareUplinkLacpPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareUplinkLacpPolicy from a JSON string
v_mware_uplink_lacp_policy_instance = VMwareUplinkLacpPolicy.from_json(json)
# print the JSON string representation of the object
print VMwareUplinkLacpPolicy.to_json()

# convert the object into a dict
v_mware_uplink_lacp_policy_dict = v_mware_uplink_lacp_policy_instance.to_dict()
# create an instance of VMwareUplinkLacpPolicy from a dict
v_mware_uplink_lacp_policy_form_dict = v_mware_uplink_lacp_policy.from_dict(v_mware_uplink_lacp_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


