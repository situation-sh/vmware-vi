# HostExtendDiskRequestType

The parameters of *HostVStorageObjectManager.HostExtendDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**new_capacity_in_mb** | **int** | The new capacity of the virtual disk in MB.  | 

## Example

```python
from vmware_vi.models.host_extend_disk_request_type import HostExtendDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostExtendDiskRequestType from a JSON string
host_extend_disk_request_type_instance = HostExtendDiskRequestType.from_json(json)
# print the JSON string representation of the object
print HostExtendDiskRequestType.to_json()

# convert the object into a dict
host_extend_disk_request_type_dict = host_extend_disk_request_type_instance.to_dict()
# create an instance of HostExtendDiskRequestType from a dict
host_extend_disk_request_type_form_dict = host_extend_disk_request_type.from_dict(host_extend_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


