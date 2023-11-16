# DeleteVirtualDiskRequestType

The parameters of *VirtualDiskManager.DeleteVirtualDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the disk, either a datastore path or a URL referring to the virtual disk to be deleted.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.delete_virtual_disk_request_type import DeleteVirtualDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVirtualDiskRequestType from a JSON string
delete_virtual_disk_request_type_instance = DeleteVirtualDiskRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteVirtualDiskRequestType.to_json()

# convert the object into a dict
delete_virtual_disk_request_type_dict = delete_virtual_disk_request_type_instance.to_dict()
# create an instance of DeleteVirtualDiskRequestType from a dict
delete_virtual_disk_request_type_form_dict = delete_virtual_disk_request_type.from_dict(delete_virtual_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


