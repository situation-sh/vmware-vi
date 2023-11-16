# VchaClusterNetworkSpec

The VchaClusterNetworkSpec class contains network configuration information for a VCHA Cluster.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**witness_network_spec** | [**NodeNetworkSpec**](NodeNetworkSpec.md) |  | 
**passive_network_spec** | [**PassiveNodeNetworkSpec**](PassiveNodeNetworkSpec.md) |  | 

## Example

```python
from vmware_vi.models.vcha_cluster_network_spec import VchaClusterNetworkSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VchaClusterNetworkSpec from a JSON string
vcha_cluster_network_spec_instance = VchaClusterNetworkSpec.from_json(json)
# print the JSON string representation of the object
print VchaClusterNetworkSpec.to_json()

# convert the object into a dict
vcha_cluster_network_spec_dict = vcha_cluster_network_spec_instance.to_dict()
# create an instance of VchaClusterNetworkSpec from a dict
vcha_cluster_network_spec_form_dict = vcha_cluster_network_spec.from_dict(vcha_cluster_network_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


