# CopyVirtualDiskRequestType

The parameters of *VirtualDiskManager.CopyVirtualDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_name** | **str** | The name of the source, either a datastore path or a URL referring to the virtual disk to be copied.  | 
**source_datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**dest_name** | **str** | The name of the destination, either a datastore path or a URL referring to the virtual disk to be created.  | 
**dest_datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**dest_spec** | [**VirtualDiskSpec**](VirtualDiskSpec.md) |  | [optional] 
**force** | **bool** | The force flag is currently ignored. The FileAlreadyExists fault is thrown if the destination file already exists.  | [optional] 

## Example

```python
from vmware_vi.models.copy_virtual_disk_request_type import CopyVirtualDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CopyVirtualDiskRequestType from a JSON string
copy_virtual_disk_request_type_instance = CopyVirtualDiskRequestType.from_json(json)
# print the JSON string representation of the object
print CopyVirtualDiskRequestType.to_json()

# convert the object into a dict
copy_virtual_disk_request_type_dict = copy_virtual_disk_request_type_instance.to_dict()
# create an instance of CopyVirtualDiskRequestType from a dict
copy_virtual_disk_request_type_form_dict = copy_virtual_disk_request_type.from_dict(copy_virtual_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


