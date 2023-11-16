# ExtendDiskRequestType

The parameters of *VcenterVStorageObjectManager.ExtendDisk_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**new_capacity_in_mb** | **int** | The new capacity of the virtual disk in MB.  | 

## Example

```python
from vmware_vi.models.extend_disk_request_type import ExtendDiskRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendDiskRequestType from a JSON string
extend_disk_request_type_instance = ExtendDiskRequestType.from_json(json)
# print the JSON string representation of the object
print ExtendDiskRequestType.to_json()

# convert the object into a dict
extend_disk_request_type_dict = extend_disk_request_type_instance.to_dict()
# create an instance of ExtendDiskRequestType from a dict
extend_disk_request_type_form_dict = extend_disk_request_type.from_dict(extend_disk_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


