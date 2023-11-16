# ArrayOfHostNetworkConfigNetStackSpec

A boxed array of *HostNetworkConfigNetStackSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostNetworkConfigNetStackSpec]**](HostNetworkConfigNetStackSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_network_config_net_stack_spec import ArrayOfHostNetworkConfigNetStackSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostNetworkConfigNetStackSpec from a JSON string
array_of_host_network_config_net_stack_spec_instance = ArrayOfHostNetworkConfigNetStackSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostNetworkConfigNetStackSpec.to_json()

# convert the object into a dict
array_of_host_network_config_net_stack_spec_dict = array_of_host_network_config_net_stack_spec_instance.to_dict()
# create an instance of ArrayOfHostNetworkConfigNetStackSpec from a dict
array_of_host_network_config_net_stack_spec_form_dict = array_of_host_network_config_net_stack_spec.from_dict(array_of_host_network_config_net_stack_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


