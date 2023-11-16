# VstorageObjectVCenterQueryChangedDiskAreasRequestType

The parameters of *VcenterVStorageObjectManager.VstorageObjectVCenterQueryChangedDiskAreas*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**snapshot_id** | [**ID**](ID.md) |  | 
**start_offset** | **int** | Start Offset in bytes at which to start computing changes. Typically, callers will make multiple calls to this function, starting with startOffset 0 and then examine the \&quot;length\&quot; property in the returned DiskChangeInfo structure, repeatedly calling queryChangedDiskAreas until a map for the entire virtual disk has been obtained.  | 
**change_id** | **str** | Identifier referring to a point in the past that should be used as the point in time at which to begin including changes to the disk in the result. A typical use case would be a backup application obtaining a changeId from a virtual disk&#39;s backing info when performing a backup. When a subsequent incremental backup is to be performed, this change Id can be used to obtain a list of changed areas on disk.  | 

## Example

```python
from vmware_vi.models.vstorage_object_v_center_query_changed_disk_areas_request_type import VstorageObjectVCenterQueryChangedDiskAreasRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of VstorageObjectVCenterQueryChangedDiskAreasRequestType from a JSON string
vstorage_object_v_center_query_changed_disk_areas_request_type_instance = VstorageObjectVCenterQueryChangedDiskAreasRequestType.from_json(json)
# print the JSON string representation of the object
print VstorageObjectVCenterQueryChangedDiskAreasRequestType.to_json()

# convert the object into a dict
vstorage_object_v_center_query_changed_disk_areas_request_type_dict = vstorage_object_v_center_query_changed_disk_areas_request_type_instance.to_dict()
# create an instance of VstorageObjectVCenterQueryChangedDiskAreasRequestType from a dict
vstorage_object_v_center_query_changed_disk_areas_request_type_form_dict = vstorage_object_v_center_query_changed_disk_areas_request_type.from_dict(vstorage_object_v_center_query_changed_disk_areas_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


