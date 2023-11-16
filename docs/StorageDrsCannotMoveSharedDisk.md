# StorageDrsCannotMoveSharedDisk

This fault is thrown because Storage DRS cannot generate recommendations to relocate a shared virtual disk that is attached to more than one Vm.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_cannot_move_shared_disk import StorageDrsCannotMoveSharedDisk

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsCannotMoveSharedDisk from a JSON string
storage_drs_cannot_move_shared_disk_instance = StorageDrsCannotMoveSharedDisk.from_json(json)
# print the JSON string representation of the object
print StorageDrsCannotMoveSharedDisk.to_json()

# convert the object into a dict
storage_drs_cannot_move_shared_disk_dict = storage_drs_cannot_move_shared_disk_instance.to_dict()
# create an instance of StorageDrsCannotMoveSharedDisk from a dict
storage_drs_cannot_move_shared_disk_form_dict = storage_drs_cannot_move_shared_disk.from_dict(storage_drs_cannot_move_shared_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


