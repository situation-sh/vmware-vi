# StoragePlacementResult

Both *StorageResourceManager.RecommendDatastores* and *Datastore.DatastoreEnterMaintenanceMode* methods may invoke Storage DRS for recommendations on placing or evacuating virtual disks.  StoragePlacementResult is the class of the result returned by the methods.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | [**List[ClusterRecommendation]**](ClusterRecommendation.md) | The list of recommendations that the client needs to approve manually.  ***Since:*** vSphere API 5.0  | [optional] 
**drs_fault** | [**ClusterDrsFaults**](ClusterDrsFaults.md) |  | [optional] 
**task** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.storage_placement_result import StoragePlacementResult

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePlacementResult from a JSON string
storage_placement_result_instance = StoragePlacementResult.from_json(json)
# print the JSON string representation of the object
print StoragePlacementResult.to_json()

# convert the object into a dict
storage_placement_result_dict = storage_placement_result_instance.to_dict()
# create an instance of StoragePlacementResult from a dict
storage_placement_result_form_dict = storage_placement_result.from_dict(storage_placement_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


