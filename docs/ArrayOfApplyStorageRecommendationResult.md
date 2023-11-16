# ArrayOfApplyStorageRecommendationResult

A boxed array of *ApplyStorageRecommendationResult*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ApplyStorageRecommendationResult]**](ApplyStorageRecommendationResult.md) |  | 

## Example

```python
from vmware_vi.models.array_of_apply_storage_recommendation_result import ArrayOfApplyStorageRecommendationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfApplyStorageRecommendationResult from a JSON string
array_of_apply_storage_recommendation_result_instance = ArrayOfApplyStorageRecommendationResult.from_json(json)
# print the JSON string representation of the object
print ArrayOfApplyStorageRecommendationResult.to_json()

# convert the object into a dict
array_of_apply_storage_recommendation_result_dict = array_of_apply_storage_recommendation_result_instance.to_dict()
# create an instance of ArrayOfApplyStorageRecommendationResult from a dict
array_of_apply_storage_recommendation_result_form_dict = array_of_apply_storage_recommendation_result.from_dict(array_of_apply_storage_recommendation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


