# HostSnmpConfigSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**port** | **int** |  | [optional] 
**read_only_communities** | **List[str]** |  | [optional] 
**trap_targets** | [**List[HostSnmpDestination]**](HostSnmpDestination.md) |  | [optional] 
**option** | [**List[KeyValue]**](KeyValue.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_snmp_config_spec import HostSnmpConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostSnmpConfigSpec from a JSON string
host_snmp_config_spec_instance = HostSnmpConfigSpec.from_json(json)
# print the JSON string representation of the object
print HostSnmpConfigSpec.to_json()

# convert the object into a dict
host_snmp_config_spec_dict = host_snmp_config_spec_instance.to_dict()
# create an instance of HostSnmpConfigSpec from a dict
host_snmp_config_spec_form_dict = host_snmp_config_spec.from_dict(host_snmp_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


