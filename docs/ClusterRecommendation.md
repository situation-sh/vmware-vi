# ClusterRecommendation

Recommendation is the base class for any packaged group of actions that are intended to take the system from one state to another one.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key to identify the recommendation when calling applyRecommendation.  ***Since:*** VI API 2.5  | 
**type** | **str** | Type of the recommendation.  This differentiates between various of recommendations aimed at achieving different goals.  ***Since:*** VI API 2.5  | 
**time** | **datetime** | The time this recommendation was computed.  ***Since:*** VI API 2.5  | 
**rating** | **int** | A rating of the recommendation.  Valid values range from 1 (lowest confidence) to 5 (highest confidence).  ***Since:*** VI API 2.5  | 
**reason** | **str** | A reason code explaining why this set of migrations is being suggested.  ***Since:*** VI API 2.5  | 
**reason_text** | **str** | Text that provides more information about the reason code for the suggested set of migrations.  ***Since:*** VI API 2.5  | 
**warning_text** | **str** | Text that provides warnings about potential adverse implications of applying this recommendation  ***Since:*** vSphere API 6.0  | [optional] 
**warning_details** | [**LocalizableMessage**](LocalizableMessage.md) |  | [optional] 
**prerequisite** | **List[str]** | This recommendation may depend on some other recommendations.  The prerequisite recommendations are listed by their keys.  ***Since:*** VI API 2.5  | [optional] 
**action** | [**List[ClusterAction]**](ClusterAction.md) | List of actions that are executed as part of this recommendation  ***Since:*** VI API 2.5  | [optional] 
**target** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_recommendation import ClusterRecommendation

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRecommendation from a JSON string
cluster_recommendation_instance = ClusterRecommendation.from_json(json)
# print the JSON string representation of the object
print ClusterRecommendation.to_json()

# convert the object into a dict
cluster_recommendation_dict = cluster_recommendation_instance.to_dict()
# create an instance of ClusterRecommendation from a dict
cluster_recommendation_form_dict = cluster_recommendation.from_dict(cluster_recommendation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


