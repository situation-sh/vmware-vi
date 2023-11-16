# ArrayOfClusterHostRecommendation

A boxed array of *ClusterHostRecommendation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterHostRecommendation]**](ClusterHostRecommendation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_host_recommendation import ArrayOfClusterHostRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterHostRecommendation from a JSON string
array_of_cluster_host_recommendation_instance = ArrayOfClusterHostRecommendation.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterHostRecommendation.to_json()

# convert the object into a dict
array_of_cluster_host_recommendation_dict = array_of_cluster_host_recommendation_instance.to_dict()
# create an instance of ArrayOfClusterHostRecommendation from a dict
array_of_cluster_host_recommendation_form_dict = array_of_cluster_host_recommendation.from_dict(array_of_cluster_host_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


