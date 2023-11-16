# PodStorageDrsEntry

An entry containing storage DRS configuration, runtime results, and history for a pod *StoragePod*.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_drs_config** | [**StorageDrsConfigInfo**](StorageDrsConfigInfo.md) |  | 
**recommendation** | [**List[ClusterRecommendation]**](ClusterRecommendation.md) | List of recommended actions for the Storage Pod.  It is possible that the current set of recommendations may be empty, either due to not having any running dynamic recommendation generation module, or since there may be no recommended actions at this time.  ***Since:*** vSphere API 5.0  | [optional] 
**drs_fault** | [**List[ClusterDrsFaults]**](ClusterDrsFaults.md) | A collection of the DRS faults generated in the last Storage DRS invocation.  Each element of the collection is the set of faults generated in one recommendation.  ***Since:*** vSphere API 5.0  | [optional] 
**action_history** | [**List[ClusterActionHistory]**](ClusterActionHistory.md) | The set of actions that have been performed recently.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.pod_storage_drs_entry import PodStorageDrsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PodStorageDrsEntry from a JSON string
pod_storage_drs_entry_instance = PodStorageDrsEntry.from_json(json)
# print the JSON string representation of the object
print PodStorageDrsEntry.to_json()

# convert the object into a dict
pod_storage_drs_entry_dict = pod_storage_drs_entry_instance.to_dict()
# create an instance of PodStorageDrsEntry from a dict
pod_storage_drs_entry_form_dict = pod_storage_drs_entry.from_dict(pod_storage_drs_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


