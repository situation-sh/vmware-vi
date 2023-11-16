# ExtendVirtualDiskRequestType

The parameters of *VirtualDiskManager.ExtendVirtualDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the disk, either a datastore path or a URL referring to the virtual disk whose capacity should be expanded.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**new_capacity_kb** | **int** | The new capacty of the virtual disk in Kb.  | 
**eager_zero** | **bool** | If true, the extended part of the disk will be explicitly filled with zeroes.  | [optional] 

## Example

```python
from vmware_vi.models.extend_virtual_disk_request_type import ExtendVirtualDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendVirtualDiskRequestType from a JSON string
extend_virtual_disk_request_type_instance = ExtendVirtualDiskRequestType.from_json(json)
# print the JSON string representation of the object
print ExtendVirtualDiskRequestType.to_json()

# convert the object into a dict
extend_virtual_disk_request_type_dict = extend_virtual_disk_request_type_instance.to_dict()
# create an instance of ExtendVirtualDiskRequestType from a dict
extend_virtual_disk_request_type_form_dict = extend_virtual_disk_request_type.from_dict(extend_virtual_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


