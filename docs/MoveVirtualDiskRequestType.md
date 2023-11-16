# MoveVirtualDiskRequestType

The parameters of *VirtualDiskManager.MoveVirtualDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_name** | **str** | The name of the source, either a datastore path or a URL referring to the virtual disk to be moved.  | 
**source_datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**dest_name** | **str** | The name of the destination, either a datastore path or a URL referring to the destination virtual disk.  | 
**dest_datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**force** | **bool** | If true, overwrite any indentically named disk at the destination. If not specified, it is assumed to be false  | [optional] 
**profile** | [**List[VirtualMachineProfileSpec]**](VirtualMachineProfileSpec.md) | User can specify new set of profile when moving virtual disk.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.move_virtual_disk_request_type import MoveVirtualDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MoveVirtualDiskRequestType from a JSON string
move_virtual_disk_request_type_instance = MoveVirtualDiskRequestType.from_json(json)
# print the JSON string representation of the object
print MoveVirtualDiskRequestType.to_json()

# convert the object into a dict
move_virtual_disk_request_type_dict = move_virtual_disk_request_type_instance.to_dict()
# create an instance of MoveVirtualDiskRequestType from a dict
move_virtual_disk_request_type_form_dict = move_virtual_disk_request_type.from_dict(move_virtual_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


