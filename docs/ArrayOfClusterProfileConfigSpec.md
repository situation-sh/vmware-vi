# ArrayOfClusterProfileConfigSpec

A boxed array of *ClusterProfileConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterProfileConfigSpec]**](ClusterProfileConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_profile_config_spec import ArrayOfClusterProfileConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterProfileConfigSpec from a JSON string
array_of_cluster_profile_config_spec_instance = ArrayOfClusterProfileConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterProfileConfigSpec.to_json()

# convert the object into a dict
array_of_cluster_profile_config_spec_dict = array_of_cluster_profile_config_spec_instance.to_dict()
# create an instance of ArrayOfClusterProfileConfigSpec from a dict
array_of_cluster_profile_config_spec_form_dict = array_of_cluster_profile_config_spec.from_dict(array_of_cluster_profile_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


