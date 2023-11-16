# QueryVirtualDiskUuidRequestType

The parameters of *VirtualDiskManager.QueryVirtualDiskUuid*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the disk, either a datastore path or a URL referring to the virtual disk from which to get SCSI inquiry page 0x83 data.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.query_virtual_disk_uuid_request_type import QueryVirtualDiskUuidRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryVirtualDiskUuidRequestType from a JSON string
query_virtual_disk_uuid_request_type_instance = QueryVirtualDiskUuidRequestType.from_json(json)
# print the JSON string representation of the object
print QueryVirtualDiskUuidRequestType.to_json()

# convert the object into a dict
query_virtual_disk_uuid_request_type_dict = query_virtual_disk_uuid_request_type_instance.to_dict()
# create an instance of QueryVirtualDiskUuidRequestType from a dict
query_virtual_disk_uuid_request_type_form_dict = query_virtual_disk_uuid_request_type.from_dict(query_virtual_disk_uuid_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


