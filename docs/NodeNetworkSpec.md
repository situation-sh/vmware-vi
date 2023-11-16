# NodeNetworkSpec

The NodeNetworkSpec class defines network specification of a node in the VCHA Cluster.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_settings** | [**CustomizationIPSettings**](CustomizationIPSettings.md) |  | 

## Example

```python
from vmware_vi.models.node_network_spec import NodeNetworkSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NodeNetworkSpec from a JSON string
node_network_spec_instance = NodeNetworkSpec.from_json(json)
# print the JSON string representation of the object
print NodeNetworkSpec.to_json()

# convert the object into a dict
node_network_spec_dict = node_network_spec_instance.to_dict()
# create an instance of NodeNetworkSpec from a dict
node_network_spec_form_dict = node_network_spec.from_dict(node_network_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


