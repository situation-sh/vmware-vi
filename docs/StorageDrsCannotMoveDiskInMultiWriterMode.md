# StorageDrsCannotMoveDiskInMultiWriterMode

This fault is thrown because Storage DRS cannot generate recommendations to relocate one or more virtual disks of a VM because the disk has multi-writer mode enabled.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_cannot_move_disk_in_multi_writer_mode import StorageDrsCannotMoveDiskInMultiWriterMode

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsCannotMoveDiskInMultiWriterMode from a JSON string
storage_drs_cannot_move_disk_in_multi_writer_mode_instance = StorageDrsCannotMoveDiskInMultiWriterMode.from_json(json)
# print the JSON string representation of the object
print StorageDrsCannotMoveDiskInMultiWriterMode.to_json()

# convert the object into a dict
storage_drs_cannot_move_disk_in_multi_writer_mode_dict = storage_drs_cannot_move_disk_in_multi_writer_mode_instance.to_dict()
# create an instance of StorageDrsCannotMoveDiskInMultiWriterMode from a dict
storage_drs_cannot_move_disk_in_multi_writer_mode_form_dict = storage_drs_cannot_move_disk_in_multi_writer_mode.from_dict(storage_drs_cannot_move_disk_in_multi_writer_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


