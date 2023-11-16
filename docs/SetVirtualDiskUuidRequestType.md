# SetVirtualDiskUuidRequestType

The parameters of *VirtualDiskManager.SetVirtualDiskUuid*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the disk, either a datastore path or a URL referring to the virtual disk whose SCSI inquiry page 0x83 data should be set.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**uuid** | **str** | The hex representation of the unique ID for this virtual disk.  | 

## Example

```python
from vmware_vi.models.set_virtual_disk_uuid_request_type import SetVirtualDiskUuidRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetVirtualDiskUuidRequestType from a JSON string
set_virtual_disk_uuid_request_type_instance = SetVirtualDiskUuidRequestType.from_json(json)
# print the JSON string representation of the object
print SetVirtualDiskUuidRequestType.to_json()

# convert the object into a dict
set_virtual_disk_uuid_request_type_dict = set_virtual_disk_uuid_request_type_instance.to_dict()
# create an instance of SetVirtualDiskUuidRequestType from a dict
set_virtual_disk_uuid_request_type_form_dict = set_virtual_disk_uuid_request_type.from_dict(set_virtual_disk_uuid_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


