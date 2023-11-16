# RefreshStorageDrsRecommendationRequestType

The parameters of *StorageResourceManager.RefreshStorageDrsRecommendation*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.refresh_storage_drs_recommendation_request_type import RefreshStorageDrsRecommendationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshStorageDrsRecommendationRequestType from a JSON string
refresh_storage_drs_recommendation_request_type_instance = RefreshStorageDrsRecommendationRequestType.from_json(json)
# print the JSON string representation of the object
print RefreshStorageDrsRecommendationRequestType.to_json()

# convert the object into a dict
refresh_storage_drs_recommendation_request_type_dict = refresh_storage_drs_recommendation_request_type_instance.to_dict()
# create an instance of RefreshStorageDrsRecommendationRequestType from a dict
refresh_storage_drs_recommendation_request_type_form_dict = refresh_storage_drs_recommendation_request_type.from_dict(refresh_storage_drs_recommendation_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


