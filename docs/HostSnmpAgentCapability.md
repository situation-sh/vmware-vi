# HostSnmpAgentCapability

A boxed *HostSnmpAgentCapability_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**HostSnmpAgentCapabilityEnum**](HostSnmpAgentCapabilityEnum.md) |  | 

## Example

```python
from vmware_vi.models.host_snmp_agent_capability import HostSnmpAgentCapability

# TODO update the JSON string below
json = "{}"
# create an instance of HostSnmpAgentCapability from a JSON string
host_snmp_agent_capability_instance = HostSnmpAgentCapability.from_json(json)
# print the JSON string representation of the object
print HostSnmpAgentCapability.to_json()

# convert the object into a dict
host_snmp_agent_capability_dict = host_snmp_agent_capability_instance.to_dict()
# create an instance of HostSnmpAgentCapability from a dict
host_snmp_agent_capability_form_dict = host_snmp_agent_capability.from_dict(host_snmp_agent_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


