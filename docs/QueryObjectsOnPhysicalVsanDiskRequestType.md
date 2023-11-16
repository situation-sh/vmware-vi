# QueryObjectsOnPhysicalVsanDiskRequestType

The parameters of *HostVsanInternalSystem.QueryObjectsOnPhysicalVsanDisk*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disks** | **List[str]** | List of VSAN disk UUIDs.  | 

## Example

```python
from vmware_vi.models.query_objects_on_physical_vsan_disk_request_type import QueryObjectsOnPhysicalVsanDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryObjectsOnPhysicalVsanDiskRequestType from a JSON string
query_objects_on_physical_vsan_disk_request_type_instance = QueryObjectsOnPhysicalVsanDiskRequestType.from_json(json)
# print the JSON string representation of the object
print QueryObjectsOnPhysicalVsanDiskRequestType.to_json()

# convert the object into a dict
query_objects_on_physical_vsan_disk_request_type_dict = query_objects_on_physical_vsan_disk_request_type_instance.to_dict()
# create an instance of QueryObjectsOnPhysicalVsanDiskRequestType from a dict
query_objects_on_physical_vsan_disk_request_type_form_dict = query_objects_on_physical_vsan_disk_request_type.from_dict(query_objects_on_physical_vsan_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


