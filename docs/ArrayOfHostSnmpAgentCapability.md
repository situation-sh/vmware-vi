# ArrayOfHostSnmpAgentCapability

A boxed array of *HostSnmpAgentCapability_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSnmpAgentCapabilityEnum]**](HostSnmpAgentCapabilityEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_snmp_agent_capability import ArrayOfHostSnmpAgentCapability

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSnmpAgentCapability from a JSON string
array_of_host_snmp_agent_capability_instance = ArrayOfHostSnmpAgentCapability.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSnmpAgentCapability.to_json()

# convert the object into a dict
array_of_host_snmp_agent_capability_dict = array_of_host_snmp_agent_capability_instance.to_dict()
# create an instance of ArrayOfHostSnmpAgentCapability from a dict
array_of_host_snmp_agent_capability_form_dict = array_of_host_snmp_agent_capability.from_dict(array_of_host_snmp_agent_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


