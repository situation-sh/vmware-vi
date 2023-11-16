# DatastoreMountPathDatastorePair

Contains a mapping of an old mount path and its corresponding resignatured or remounted datastore  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_mount_path** | **str** | Old file path where file system volume is mounted, which should be *path* value in *HostMountInfo*  ***Since:*** vSphere API 4.1  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.datastore_mount_path_datastore_pair import DatastoreMountPathDatastorePair

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreMountPathDatastorePair from a JSON string
datastore_mount_path_datastore_pair_instance = DatastoreMountPathDatastorePair.from_json(json)
# print the JSON string representation of the object
print DatastoreMountPathDatastorePair.to_json()

# convert the object into a dict
datastore_mount_path_datastore_pair_dict = datastore_mount_path_datastore_pair_instance.to_dict()
# create an instance of DatastoreMountPathDatastorePair from a dict
datastore_mount_path_datastore_pair_form_dict = datastore_mount_path_datastore_pair.from_dict(datastore_mount_path_datastore_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


