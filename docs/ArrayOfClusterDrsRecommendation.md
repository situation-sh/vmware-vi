# ArrayOfClusterDrsRecommendation

A boxed array of *ClusterDrsRecommendation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterDrsRecommendation]**](ClusterDrsRecommendation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_drs_recommendation import ArrayOfClusterDrsRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterDrsRecommendation from a JSON string
array_of_cluster_drs_recommendation_instance = ArrayOfClusterDrsRecommendation.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterDrsRecommendation.to_json()

# convert the object into a dict
array_of_cluster_drs_recommendation_dict = array_of_cluster_drs_recommendation_instance.to_dict()
# create an instance of ArrayOfClusterDrsRecommendation from a dict
array_of_cluster_drs_recommendation_form_dict = array_of_cluster_drs_recommendation.from_dict(array_of_cluster_drs_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


