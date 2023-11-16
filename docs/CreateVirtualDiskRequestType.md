# CreateVirtualDiskRequestType

The parameters of *VirtualDiskManager.CreateVirtualDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the disk, either a datastore path or a URL referring to the virtual disk to be created.  | 
**datacenter** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**spec** | [**VirtualDiskSpec**](VirtualDiskSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_virtual_disk_request_type import CreateVirtualDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVirtualDiskRequestType from a JSON string
create_virtual_disk_request_type_instance = CreateVirtualDiskRequestType.from_json(json)
# print the JSON string representation of the object
print CreateVirtualDiskRequestType.to_json()

# convert the object into a dict
create_virtual_disk_request_type_dict = create_virtual_disk_request_type_instance.to_dict()
# create an instance of CreateVirtualDiskRequestType from a dict
create_virtual_disk_request_type_form_dict = create_virtual_disk_request_type.from_dict(create_virtual_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


