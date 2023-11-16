# StoragePodSummary

The *StoragePodSummary* data object encapsulates runtime properties of a *StoragePod*.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the storage pod.  ***Since:*** vSphere API 5.0  | 
**capacity** | **int** | Total capacity of this storage pod, in bytes.  This value is the sum of the capacity of all datastores that are part of this storage pod, and is updated periodically by the server.  ***Since:*** vSphere API 5.0  | 
**free_space** | **int** | Total free space on this storage pod, in bytes.  This value is the sum of the free space on all datastores that are part of this storage pod, and is updated periodically by the server.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.storage_pod_summary import StoragePodSummary

# TODO update the JSON string below
json = "{}"
# create an instance of StoragePodSummary from a JSON string
storage_pod_summary_instance = StoragePodSummary.from_json(json)
# print the JSON string representation of the object
print StoragePodSummary.to_json()

# convert the object into a dict
storage_pod_summary_dict = storage_pod_summary_instance.to_dict()
# create an instance of StoragePodSummary from a dict
storage_pod_summary_form_dict = storage_pod_summary.from_dict(storage_pod_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


