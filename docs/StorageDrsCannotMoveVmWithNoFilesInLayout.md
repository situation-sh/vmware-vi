# StorageDrsCannotMoveVmWithNoFilesInLayout

This fault is thrown because Storage DRS cannot generate recommendations to relocate VMs that have no files in its file layout.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_cannot_move_vm_with_no_files_in_layout import StorageDrsCannotMoveVmWithNoFilesInLayout

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsCannotMoveVmWithNoFilesInLayout from a JSON string
storage_drs_cannot_move_vm_with_no_files_in_layout_instance = StorageDrsCannotMoveVmWithNoFilesInLayout.from_json(json)
# print the JSON string representation of the object
print StorageDrsCannotMoveVmWithNoFilesInLayout.to_json()

# convert the object into a dict
storage_drs_cannot_move_vm_with_no_files_in_layout_dict = storage_drs_cannot_move_vm_with_no_files_in_layout_instance.to_dict()
# create an instance of StorageDrsCannotMoveVmWithNoFilesInLayout from a dict
storage_drs_cannot_move_vm_with_no_files_in_layout_form_dict = storage_drs_cannot_move_vm_with_no_files_in_layout.from_dict(storage_drs_cannot_move_vm_with_no_files_in_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


