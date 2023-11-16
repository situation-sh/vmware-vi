# QueryChangedDiskAreasRequestType

The parameters of *VirtualMachine.QueryChangedDiskAreas*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**device_key** | **int** | Identifies the virtual disk for which to compute changes.  | 
**start_offset** | **int** | Start Offset in bytes at which to start computing changes. Typically, callers will make multiple calls to this function, starting with startOffset 0 and then examine the \&quot;length\&quot; property in the returned DiskChangeInfo structure, repeatedly calling queryChangedDiskAreas until a map forthe entire virtual disk has been obtained.  | 
**change_id** | **str** | Identifyer referring to a point in the past that should be used as the point in time at which to begin including changes to the disk in the result. A typical use case would be a backup application obtaining a changeId from a virtual disk&#39;s backing info when performing a backup. When a subsequent incremental backup is to be performed, this change Id can be used to obtain a list of changed areas on disk.  | 

## Example

```python
from vmware_vi.models.query_changed_disk_areas_request_type import QueryChangedDiskAreasRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryChangedDiskAreasRequestType from a JSON string
query_changed_disk_areas_request_type_instance = QueryChangedDiskAreasRequestType.from_json(json)
# print the JSON string representation of the object
print QueryChangedDiskAreasRequestType.to_json()

# convert the object into a dict
query_changed_disk_areas_request_type_dict = query_changed_disk_areas_request_type_instance.to_dict()
# create an instance of QueryChangedDiskAreasRequestType from a dict
query_changed_disk_areas_request_type_form_dict = query_changed_disk_areas_request_type.from_dict(query_changed_disk_areas_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


