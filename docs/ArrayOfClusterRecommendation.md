# ArrayOfClusterRecommendation

A boxed array of *ClusterRecommendation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterRecommendation]**](ClusterRecommendation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_recommendation import ArrayOfClusterRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterRecommendation from a JSON string
array_of_cluster_recommendation_instance = ArrayOfClusterRecommendation.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterRecommendation.to_json()

# convert the object into a dict
array_of_cluster_recommendation_dict = array_of_cluster_recommendation_instance.to_dict()
# create an instance of ArrayOfClusterRecommendation from a dict
array_of_cluster_recommendation_form_dict = array_of_cluster_recommendation.from_dict(array_of_cluster_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


