# RefreshStorageDrsRecommendationsForPodRequestType

The parameters of *StorageResourceManager.RefreshStorageDrsRecommendationsForPod_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.refresh_storage_drs_recommendations_for_pod_request_type import RefreshStorageDrsRecommendationsForPodRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshStorageDrsRecommendationsForPodRequestType from a JSON string
refresh_storage_drs_recommendations_for_pod_request_type_instance = RefreshStorageDrsRecommendationsForPodRequestType.from_json(json)
# print the JSON string representation of the object
print RefreshStorageDrsRecommendationsForPodRequestType.to_json()

# convert the object into a dict
refresh_storage_drs_recommendations_for_pod_request_type_dict = refresh_storage_drs_recommendations_for_pod_request_type_instance.to_dict()
# create an instance of RefreshStorageDrsRecommendationsForPodRequestType from a dict
refresh_storage_drs_recommendations_for_pod_request_type_form_dict = refresh_storage_drs_recommendations_for_pod_request_type.from_dict(refresh_storage_drs_recommendations_for_pod_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


