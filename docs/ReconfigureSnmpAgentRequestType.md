# ReconfigureSnmpAgentRequestType

The parameters of *HostSnmpSystem.ReconfigureSnmpAgent*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostSnmpConfigSpec**](HostSnmpConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.reconfigure_snmp_agent_request_type import ReconfigureSnmpAgentRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigureSnmpAgentRequestType from a JSON string
reconfigure_snmp_agent_request_type_instance = ReconfigureSnmpAgentRequestType.from_json(json)
# print the JSON string representation of the object
print ReconfigureSnmpAgentRequestType.to_json()

# convert the object into a dict
reconfigure_snmp_agent_request_type_dict = reconfigure_snmp_agent_request_type_instance.to_dict()
# create an instance of ReconfigureSnmpAgentRequestType from a dict
reconfigure_snmp_agent_request_type_form_dict = reconfigure_snmp_agent_request_type.from_dict(reconfigure_snmp_agent_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


