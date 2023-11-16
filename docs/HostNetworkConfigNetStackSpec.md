# HostNetworkConfigNetStackSpec

This data type describes Network Stack Spec  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**net_stack_instance** | [**HostNetStackInstance**](HostNetStackInstance.md) |  | 
**operation** | **str** | Operation type, see *ConfigSpecOperation_enum* for valid values.  Only edit operation is supported currently.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.host_network_config_net_stack_spec import HostNetworkConfigNetStackSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostNetworkConfigNetStackSpec from a JSON string
host_network_config_net_stack_spec_instance = HostNetworkConfigNetStackSpec.from_json(json)
# print the JSON string representation of the object
print HostNetworkConfigNetStackSpec.to_json()

# convert the object into a dict
host_network_config_net_stack_spec_dict = host_network_config_net_stack_spec_instance.to_dict()
# create an instance of HostNetworkConfigNetStackSpec from a dict
host_network_config_net_stack_spec_form_dict = host_network_config_net_stack_spec.from_dict(host_network_config_net_stack_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


