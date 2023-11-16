# ApplyStorageRecommendationResult

Both *StorageResourceManager.RecommendDatastores* and *Datastore.DatastoreEnterMaintenanceMode* methods may invoke Storage DRS for recommendations on placing or evacuating virtual disks.  All initial placement recommendations, and some enterMaintenanceMode recommendations need to be approved by the user. Recommendations that are approved will be applied using the *StorageResourceManager.ApplyStorageDrsRecommendation_Task* method. This class encapsulates the result of applying a subset of the recommendations.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.apply_storage_recommendation_result import ApplyStorageRecommendationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyStorageRecommendationResult from a JSON string
apply_storage_recommendation_result_instance = ApplyStorageRecommendationResult.from_json(json)
# print the JSON string representation of the object
print ApplyStorageRecommendationResult.to_json()

# convert the object into a dict
apply_storage_recommendation_result_dict = apply_storage_recommendation_result_instance.to_dict()
# create an instance of ApplyStorageRecommendationResult from a dict
apply_storage_recommendation_result_form_dict = apply_storage_recommendation_result.from_dict(apply_storage_recommendation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


