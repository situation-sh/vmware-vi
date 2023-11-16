# ArrayOfHostSnmpSystemAgentLimits

A boxed array of *HostSnmpSystemAgentLimits*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSnmpSystemAgentLimits]**](HostSnmpSystemAgentLimits.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_snmp_system_agent_limits import ArrayOfHostSnmpSystemAgentLimits

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSnmpSystemAgentLimits from a JSON string
array_of_host_snmp_system_agent_limits_instance = ArrayOfHostSnmpSystemAgentLimits.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSnmpSystemAgentLimits.to_json()

# convert the object into a dict
array_of_host_snmp_system_agent_limits_dict = array_of_host_snmp_system_agent_limits_instance.to_dict()
# create an instance of ArrayOfHostSnmpSystemAgentLimits from a dict
array_of_host_snmp_system_agent_limits_form_dict = array_of_host_snmp_system_agent_limits.from_dict(array_of_host_snmp_system_agent_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


