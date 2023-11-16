# ArrayOfClusterNetworkConfigSpec

A boxed array of *ClusterNetworkConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterNetworkConfigSpec]**](ClusterNetworkConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_network_config_spec import ArrayOfClusterNetworkConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterNetworkConfigSpec from a JSON string
array_of_cluster_network_config_spec_instance = ArrayOfClusterNetworkConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterNetworkConfigSpec.to_json()

# convert the object into a dict
array_of_cluster_network_config_spec_dict = array_of_cluster_network_config_spec_instance.to_dict()
# create an instance of ArrayOfClusterNetworkConfigSpec from a dict
array_of_cluster_network_config_spec_form_dict = array_of_cluster_network_config_spec.from_dict(array_of_cluster_network_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


