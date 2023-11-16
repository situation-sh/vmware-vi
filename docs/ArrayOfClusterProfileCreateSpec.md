# ArrayOfClusterProfileCreateSpec

A boxed array of *ClusterProfileCreateSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterProfileCreateSpec]**](ClusterProfileCreateSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_profile_create_spec import ArrayOfClusterProfileCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterProfileCreateSpec from a JSON string
array_of_cluster_profile_create_spec_instance = ArrayOfClusterProfileCreateSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterProfileCreateSpec.to_json()

# convert the object into a dict
array_of_cluster_profile_create_spec_dict = array_of_cluster_profile_create_spec_instance.to_dict()
# create an instance of ArrayOfClusterProfileCreateSpec from a dict
array_of_cluster_profile_create_spec_form_dict = array_of_cluster_profile_create_spec.from_dict(array_of_cluster_profile_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


