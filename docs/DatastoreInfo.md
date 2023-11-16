# DatastoreInfo

Detailed information about a datastore.  This is a base type for derived types that have more specific details about a datastore.  See also *HostVmfsVolume*, *HostNasVolume*, *HostLocalFileSystemVolume*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the datastore.  | 
**url** | **str** | The unique locator for the datastore.  | 
**free_space** | **int** | Free space of this datastore, in bytes.  The server periodically updates this value. It can be explicitly refreshed with the Refresh operation.  | 
**max_file_size** | **int** | The maximum size of a file that can reside on this file system volume.  | 
**max_virtual_disk_capacity** | **int** | The maximum capacity of a virtual disk which can be created on this volume.  ***Since:*** vSphere API 5.5  | [optional] 
**max_memory_file_size** | **int** | The maximum size of a snapshot or a swap file that can reside on this file system volume.  ***Since:*** vSphere API 6.0  | 
**timestamp** | **datetime** | Time when the free-space and capacity values in *DatastoreInfo* and *DatastoreSummary* were updated.  ***Since:*** vSphere API 4.0  | [optional] 
**container_id** | **str** | The unique container ID of the datastore, if applicable.  ***Since:*** vSphere API 5.5  | [optional] 
**alias_of** | **str** | vSAN datastore container that this datastore is alias of.  If this field is unset then this datastore is not alias of any other vSAN datastore. See *DatastoreInfo.containerId*.  ***Since:*** vSphere API 6.7.1  | [optional] 

## Example

```python
from vmware_vi.models.datastore_info import DatastoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreInfo from a JSON string
datastore_info_instance = DatastoreInfo.from_json(json)
# print the JSON string representation of the object
print DatastoreInfo.to_json()

# convert the object into a dict
datastore_info_dict = datastore_info_instance.to_dict()
# create an instance of DatastoreInfo from a dict
datastore_info_form_dict = datastore_info.from_dict(datastore_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


