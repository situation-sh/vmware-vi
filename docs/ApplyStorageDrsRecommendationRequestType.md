# ApplyStorageDrsRecommendationRequestType

The parameters of *StorageResourceManager.ApplyStorageDrsRecommendation_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **List[str]** | The key fields of the Recommendations that are applied.  | 

## Example

```python
from vmware_vi.models.apply_storage_drs_recommendation_request_type import ApplyStorageDrsRecommendationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyStorageDrsRecommendationRequestType from a JSON string
apply_storage_drs_recommendation_request_type_instance = ApplyStorageDrsRecommendationRequestType.from_json(json)
# print the JSON string representation of the object
print ApplyStorageDrsRecommendationRequestType.to_json()

# convert the object into a dict
apply_storage_drs_recommendation_request_type_dict = apply_storage_drs_recommendation_request_type_instance.to_dict()
# create an instance of ApplyStorageDrsRecommendationRequestType from a dict
apply_storage_drs_recommendation_request_type_form_dict = apply_storage_drs_recommendation_request_type.from_dict(apply_storage_drs_recommendation_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


