# DefragmentVirtualDiskRequestType

The parameters of *VirtualDiskManager.DefragmentVirtualDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the disk, either a datastore path or a URL referring to the virtual disk that should be defragmented.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.defragment_virtual_disk_request_type import DefragmentVirtualDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DefragmentVirtualDiskRequestType from a JSON string
defragment_virtual_disk_request_type_instance = DefragmentVirtualDiskRequestType.from_json(json)
# print the JSON string representation of the object
print DefragmentVirtualDiskRequestType.to_json()

# convert the object into a dict
defragment_virtual_disk_request_type_dict = defragment_virtual_disk_request_type_instance.to_dict()
# create an instance of DefragmentVirtualDiskRequestType from a dict
defragment_virtual_disk_request_type_form_dict = defragment_virtual_disk_request_type.from_dict(defragment_virtual_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


