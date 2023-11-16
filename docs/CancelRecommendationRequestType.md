# CancelRecommendationRequestType

The parameters of *ClusterComputeResource.CancelRecommendation*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key field of the Recommendation.  | 

## Example

```python
from vmware_vi.models.cancel_recommendation_request_type import CancelRecommendationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CancelRecommendationRequestType from a JSON string
cancel_recommendation_request_type_instance = CancelRecommendationRequestType.from_json(json)
# print the JSON string representation of the object
print CancelRecommendationRequestType.to_json()

# convert the object into a dict
cancel_recommendation_request_type_dict = cancel_recommendation_request_type_instance.to_dict()
# create an instance of CancelRecommendationRequestType from a dict
cancel_recommendation_request_type_form_dict = cancel_recommendation_request_type.from_dict(cancel_recommendation_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


