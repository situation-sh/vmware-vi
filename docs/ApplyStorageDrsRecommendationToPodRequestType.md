# ApplyStorageDrsRecommendationToPodRequestType

The parameters of *StorageResourceManager.ApplyStorageDrsRecommendationToPod_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**key** | **str** | The key field of the Recommendation.  | 

## Example

```python
from vmware_vi.models.apply_storage_drs_recommendation_to_pod_request_type import ApplyStorageDrsRecommendationToPodRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyStorageDrsRecommendationToPodRequestType from a JSON string
apply_storage_drs_recommendation_to_pod_request_type_instance = ApplyStorageDrsRecommendationToPodRequestType.from_json(json)
# print the JSON string representation of the object
print ApplyStorageDrsRecommendationToPodRequestType.to_json()

# convert the object into a dict
apply_storage_drs_recommendation_to_pod_request_type_dict = apply_storage_drs_recommendation_to_pod_request_type_instance.to_dict()
# create an instance of ApplyStorageDrsRecommendationToPodRequestType from a dict
apply_storage_drs_recommendation_to_pod_request_type_form_dict = apply_storage_drs_recommendation_to_pod_request_type.from_dict(apply_storage_drs_recommendation_to_pod_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


