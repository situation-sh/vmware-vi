# DVSNameArrayUplinkPortPolicy

The uplink port policy specifies an array of uniform names for the uplink ports across the hosts.  The size of the array indicates the number of uplink ports that will be created for each host in the switch.  When the names in this array change, the uplink ports on all the hosts are automatically renamed accordingly. Increasing the number of names in the array automatically creates additional uplink ports bearing the added name on each host. Decreasing the number of name automatically deletes the unused uplink ports on each host. Decreasing beyond the number of unused uplink port raises a fault.  This policy overrides the portgroup port naming format (*DVPortgroupConfigSpec*.*DVPortgroupConfigSpec.portNameFormat*), if both are defined and the uplink ports are created in a uplink portgroup.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uplink_port_name** | **List[str]** | The uniform name of uplink ports on each host.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.dvs_name_array_uplink_port_policy import DVSNameArrayUplinkPortPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DVSNameArrayUplinkPortPolicy from a JSON string
dvs_name_array_uplink_port_policy_instance = DVSNameArrayUplinkPortPolicy.from_json(json)
# print the JSON string representation of the object
print DVSNameArrayUplinkPortPolicy.to_json()

# convert the object into a dict
dvs_name_array_uplink_port_policy_dict = dvs_name_array_uplink_port_policy_instance.to_dict()
# create an instance of DVSNameArrayUplinkPortPolicy from a dict
dvs_name_array_uplink_port_policy_form_dict = dvs_name_array_uplink_port_policy.from_dict(dvs_name_array_uplink_port_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


