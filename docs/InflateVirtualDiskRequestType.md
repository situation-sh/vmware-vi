# InflateVirtualDiskRequestType

The parameters of *VirtualDiskManager.InflateVirtualDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the disk, either a datastore path or a URL referring to the virtual disk that should be inflated.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.inflate_virtual_disk_request_type import InflateVirtualDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of InflateVirtualDiskRequestType from a JSON string
inflate_virtual_disk_request_type_instance = InflateVirtualDiskRequestType.from_json(json)
# print the JSON string representation of the object
print InflateVirtualDiskRequestType.to_json()

# convert the object into a dict
inflate_virtual_disk_request_type_dict = inflate_virtual_disk_request_type_instance.to_dict()
# create an instance of InflateVirtualDiskRequestType from a dict
inflate_virtual_disk_request_type_form_dict = inflate_virtual_disk_request_type.from_dict(inflate_virtual_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


