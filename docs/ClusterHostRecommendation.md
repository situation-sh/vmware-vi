# ClusterHostRecommendation

A DRS recommended host for either powering on, resuming or reverting a virtual machine, or migrating a virtual machine from outside the cluster. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**rating** | **int** | Rating for the recommendation.  Ratings range from 1 to 5, and the higher the rating, the stronger DRS suggests this host is picked for the operation.  | 

## Example

```python
from vmware_vi.models.cluster_host_recommendation import ClusterHostRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterHostRecommendation from a JSON string
cluster_host_recommendation_instance = ClusterHostRecommendation.from_json(json)
# print the JSON string representation of the object
print ClusterHostRecommendation.to_json()

# convert the object into a dict
cluster_host_recommendation_dict = cluster_host_recommendation_instance.to_dict()
# create an instance of ClusterHostRecommendation from a dict
cluster_host_recommendation_form_dict = cluster_host_recommendation.from_dict(cluster_host_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


