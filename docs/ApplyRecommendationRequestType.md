# ApplyRecommendationRequestType

The parameters of *ClusterComputeResource.ApplyRecommendation*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key field of the DrsRecommendation or Recommendation.  | 

## Example

```python
from vmware_vi.models.apply_recommendation_request_type import ApplyRecommendationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyRecommendationRequestType from a JSON string
apply_recommendation_request_type_instance = ApplyRecommendationRequestType.from_json(json)
# print the JSON string representation of the object
print ApplyRecommendationRequestType.to_json()

# convert the object into a dict
apply_recommendation_request_type_dict = apply_recommendation_request_type_instance.to_dict()
# create an instance of ApplyRecommendationRequestType from a dict
apply_recommendation_request_type_form_dict = apply_recommendation_request_type.from_dict(apply_recommendation_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


