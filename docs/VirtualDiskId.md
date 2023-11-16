# VirtualDiskId

Identifier for a virtual disk.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**disk_id** | **int** | Device ID *VirtualDevice.key* of the virtual disk.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.virtual_disk_id import VirtualDiskId

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskId from a JSON string
virtual_disk_id_instance = VirtualDiskId.from_json(json)
# print the JSON string representation of the object
print VirtualDiskId.to_json()

# convert the object into a dict
virtual_disk_id_dict = virtual_disk_id_instance.to_dict()
# create an instance of VirtualDiskId from a dict
virtual_disk_id_form_dict = virtual_disk_id.from_dict(virtual_disk_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


