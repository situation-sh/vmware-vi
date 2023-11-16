# EagerZeroVirtualDiskRequestType

The parameters of *VirtualDiskManager.EagerZeroVirtualDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the disk, either a datastore path or a URL referring to the virtual disk that should be inflated.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.eager_zero_virtual_disk_request_type import EagerZeroVirtualDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of EagerZeroVirtualDiskRequestType from a JSON string
eager_zero_virtual_disk_request_type_instance = EagerZeroVirtualDiskRequestType.from_json(json)
# print the JSON string representation of the object
print EagerZeroVirtualDiskRequestType.to_json()

# convert the object into a dict
eager_zero_virtual_disk_request_type_dict = eager_zero_virtual_disk_request_type_instance.to_dict()
# create an instance of EagerZeroVirtualDiskRequestType from a dict
eager_zero_virtual_disk_request_type_form_dict = eager_zero_virtual_disk_request_type.from_dict(eager_zero_virtual_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


