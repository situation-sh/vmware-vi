# ArrayOfClusterConfigSpec

A boxed array of *ClusterConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterConfigSpec]**](ClusterConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_config_spec import ArrayOfClusterConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterConfigSpec from a JSON string
array_of_cluster_config_spec_instance = ArrayOfClusterConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterConfigSpec.to_json()

# convert the object into a dict
array_of_cluster_config_spec_dict = array_of_cluster_config_spec_instance.to_dict()
# create an instance of ArrayOfClusterConfigSpec from a dict
array_of_cluster_config_spec_form_dict = array_of_cluster_config_spec.from_dict(array_of_cluster_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


