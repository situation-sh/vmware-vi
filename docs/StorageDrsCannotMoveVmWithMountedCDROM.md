# StorageDrsCannotMoveVmWithMountedCDROM

This fault is thrown because Storage DRS cannot generate recommendations to relocate VMs that have a CD-ROM device mounted.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_cannot_move_vm_with_mounted_cdrom import StorageDrsCannotMoveVmWithMountedCDROM

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsCannotMoveVmWithMountedCDROM from a JSON string
storage_drs_cannot_move_vm_with_mounted_cdrom_instance = StorageDrsCannotMoveVmWithMountedCDROM.from_json(json)
# print the JSON string representation of the object
print StorageDrsCannotMoveVmWithMountedCDROM.to_json()

# convert the object into a dict
storage_drs_cannot_move_vm_with_mounted_cdrom_dict = storage_drs_cannot_move_vm_with_mounted_cdrom_instance.to_dict()
# create an instance of StorageDrsCannotMoveVmWithMountedCDROM from a dict
storage_drs_cannot_move_vm_with_mounted_cdrom_form_dict = storage_drs_cannot_move_vm_with_mounted_cdrom.from_dict(storage_drs_cannot_move_vm_with_mounted_cdrom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


