# ClusterNetworkConfigSpec

The Cluster network config spec allows specification of the second network adapter is used for communication between the nodes of a VCHA cluster.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_port_group** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**ip_settings** | [**CustomizationIPSettings**](CustomizationIPSettings.md) |  | 

## Example

```python
from vmware_vi.models.cluster_network_config_spec import ClusterNetworkConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterNetworkConfigSpec from a JSON string
cluster_network_config_spec_instance = ClusterNetworkConfigSpec.from_json(json)
# print the JSON string representation of the object
print ClusterNetworkConfigSpec.to_json()

# convert the object into a dict
cluster_network_config_spec_dict = cluster_network_config_spec_instance.to_dict()
# create an instance of ClusterNetworkConfigSpec from a dict
cluster_network_config_spec_form_dict = cluster_network_config_spec.from_dict(cluster_network_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


