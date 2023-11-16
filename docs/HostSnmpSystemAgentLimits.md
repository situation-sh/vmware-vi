# HostSnmpSystemAgentLimits


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_read_only_communities** | **int** | number of allowed communities  ***Since:*** VI API 2.5  | 
**max_trap_destinations** | **int** | number of allowed destinations for notifications  ***Since:*** VI API 2.5  | 
**max_community_length** | **int** | Max length of community  ***Since:*** VI API 2.5  | 
**max_buffer_size** | **int** | SNMP input buffer size  ***Since:*** VI API 2.5  | 
**capability** | [**HostSnmpAgentCapabilityEnum**](HostSnmpAgentCapabilityEnum.md) |  | 

## Example

```python
from vmware_vi.models.host_snmp_system_agent_limits import HostSnmpSystemAgentLimits

# TODO update the JSON string below
json = "{}"
# create an instance of HostSnmpSystemAgentLimits from a JSON string
host_snmp_system_agent_limits_instance = HostSnmpSystemAgentLimits.from_json(json)
# print the JSON string representation of the object
print HostSnmpSystemAgentLimits.to_json()

# convert the object into a dict
host_snmp_system_agent_limits_dict = host_snmp_system_agent_limits_instance.to_dict()
# create an instance of HostSnmpSystemAgentLimits from a dict
host_snmp_system_agent_limits_form_dict = host_snmp_system_agent_limits.from_dict(host_snmp_system_agent_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


