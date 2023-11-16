# ClusterTagCategoryUpdateSpec

An incremental update to a TagCategory list.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_tag_category_update_spec import ClusterTagCategoryUpdateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterTagCategoryUpdateSpec from a JSON string
cluster_tag_category_update_spec_instance = ClusterTagCategoryUpdateSpec.from_json(json)
# print the JSON string representation of the object
print ClusterTagCategoryUpdateSpec.to_json()

# convert the object into a dict
cluster_tag_category_update_spec_dict = cluster_tag_category_update_spec_instance.to_dict()
# create an instance of ClusterTagCategoryUpdateSpec from a dict
cluster_tag_category_update_spec_form_dict = cluster_tag_category_update_spec.from_dict(cluster_tag_category_update_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


