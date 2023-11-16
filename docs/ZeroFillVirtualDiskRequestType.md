# ZeroFillVirtualDiskRequestType

The parameters of *VirtualDiskManager.ZeroFillVirtualDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the disk, either a datastore path or a URL referring to the virtual disk whose blocks should be overwritten with zeroes.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.zero_fill_virtual_disk_request_type import ZeroFillVirtualDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ZeroFillVirtualDiskRequestType from a JSON string
zero_fill_virtual_disk_request_type_instance = ZeroFillVirtualDiskRequestType.from_json(json)
# print the JSON string representation of the object
print ZeroFillVirtualDiskRequestType.to_json()

# convert the object into a dict
zero_fill_virtual_disk_request_type_dict = zero_fill_virtual_disk_request_type_instance.to_dict()
# create an instance of ZeroFillVirtualDiskRequestType from a dict
zero_fill_virtual_disk_request_type_form_dict = zero_fill_virtual_disk_request_type.from_dict(zero_fill_virtual_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


