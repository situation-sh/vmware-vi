# ClusterDasHostRecommendation

A host recommendation for a virtual machine managed by the VMware HA Service.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**drs_rating** | **int** | Rating as computed by DRS for a DRS-enabled cluster.  Rating range from 1 to 5, and the higher the rating, the stronger DRS suggests this host is picked for the operation.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_das_host_recommendation import ClusterDasHostRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDasHostRecommendation from a JSON string
cluster_das_host_recommendation_instance = ClusterDasHostRecommendation.from_json(json)
# print the JSON string representation of the object
print ClusterDasHostRecommendation.to_json()

# convert the object into a dict
cluster_das_host_recommendation_dict = cluster_das_host_recommendation_instance.to_dict()
# create an instance of ClusterDasHostRecommendation from a dict
cluster_das_host_recommendation_form_dict = cluster_das_host_recommendation.from_dict(cluster_das_host_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


