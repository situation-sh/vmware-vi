# ArrayOfClusterTagCategoryUpdateSpec

A boxed array of *ClusterTagCategoryUpdateSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterTagCategoryUpdateSpec]**](ClusterTagCategoryUpdateSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_tag_category_update_spec import ArrayOfClusterTagCategoryUpdateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterTagCategoryUpdateSpec from a JSON string
array_of_cluster_tag_category_update_spec_instance = ArrayOfClusterTagCategoryUpdateSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterTagCategoryUpdateSpec.to_json()

# convert the object into a dict
array_of_cluster_tag_category_update_spec_dict = array_of_cluster_tag_category_update_spec_instance.to_dict()
# create an instance of ArrayOfClusterTagCategoryUpdateSpec from a dict
array_of_cluster_tag_category_update_spec_form_dict = array_of_cluster_tag_category_update_spec.from_dict(array_of_cluster_tag_category_update_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


