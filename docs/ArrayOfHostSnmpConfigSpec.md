# ArrayOfHostSnmpConfigSpec

A boxed array of *HostSnmpConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSnmpConfigSpec]**](HostSnmpConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_snmp_config_spec import ArrayOfHostSnmpConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSnmpConfigSpec from a JSON string
array_of_host_snmp_config_spec_instance = ArrayOfHostSnmpConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSnmpConfigSpec.to_json()

# convert the object into a dict
array_of_host_snmp_config_spec_dict = array_of_host_snmp_config_spec_instance.to_dict()
# create an instance of ArrayOfHostSnmpConfigSpec from a dict
array_of_host_snmp_config_spec_form_dict = array_of_host_snmp_config_spec.from_dict(array_of_host_snmp_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


