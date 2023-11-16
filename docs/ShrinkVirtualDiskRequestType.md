# ShrinkVirtualDiskRequestType

The parameters of *VirtualDiskManager.ShrinkVirtualDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the disk, either a datastore path or a URL referring to the virtual disk that should be shrink.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**copy** | **bool** | If true or omitted, performs shrink in copy-shrink mode, otherwise shrink in in-place mode.  | [optional] 

## Example

```python
from vmware_vi.models.shrink_virtual_disk_request_type import ShrinkVirtualDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ShrinkVirtualDiskRequestType from a JSON string
shrink_virtual_disk_request_type_instance = ShrinkVirtualDiskRequestType.from_json(json)
# print the JSON string representation of the object
print ShrinkVirtualDiskRequestType.to_json()

# convert the object into a dict
shrink_virtual_disk_request_type_dict = shrink_virtual_disk_request_type_instance.to_dict()
# create an instance of ShrinkVirtualDiskRequestType from a dict
shrink_virtual_disk_request_type_form_dict = shrink_virtual_disk_request_type.from_dict(shrink_virtual_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


