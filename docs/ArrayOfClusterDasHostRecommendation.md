# ArrayOfClusterDasHostRecommendation

A boxed array of *ClusterDasHostRecommendation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ClusterDasHostRecommendation]**](ClusterDasHostRecommendation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_cluster_das_host_recommendation import ArrayOfClusterDasHostRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfClusterDasHostRecommendation from a JSON string
array_of_cluster_das_host_recommendation_instance = ArrayOfClusterDasHostRecommendation.from_json(json)
# print the JSON string representation of the object
print ArrayOfClusterDasHostRecommendation.to_json()

# convert the object into a dict
array_of_cluster_das_host_recommendation_dict = array_of_cluster_das_host_recommendation_instance.to_dict()
# create an instance of ArrayOfClusterDasHostRecommendation from a dict
array_of_cluster_das_host_recommendation_form_dict = array_of_cluster_das_host_recommendation.from_dict(array_of_cluster_das_host_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


