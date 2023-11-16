# PassiveNodeNetworkSpec

The PassiveNodeNetworkSpec class defines VCHA Failover and Cluster network configuration of the Passive node VM in the VCHA Cluster.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_ip_settings** | [**CustomizationIPSettings**](CustomizationIPSettings.md) |  | [optional] 

## Example

```python
from vmware_vi.models.passive_node_network_spec import PassiveNodeNetworkSpec

# TODO update the JSON string below
json = "{}"
# create an instance of PassiveNodeNetworkSpec from a JSON string
passive_node_network_spec_instance = PassiveNodeNetworkSpec.from_json(json)
# print the JSON string representation of the object
print PassiveNodeNetworkSpec.to_json()

# convert the object into a dict
passive_node_network_spec_dict = passive_node_network_spec_instance.to_dict()
# create an instance of PassiveNodeNetworkSpec from a dict
passive_node_network_spec_form_dict = passive_node_network_spec.from_dict(passive_node_network_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


