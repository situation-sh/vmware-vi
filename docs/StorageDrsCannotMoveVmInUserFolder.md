# StorageDrsCannotMoveVmInUserFolder

This fault is thrown because Storage DRS cannot generate recommendations to relocate VMs placed in user-specified folders.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_cannot_move_vm_in_user_folder import StorageDrsCannotMoveVmInUserFolder

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsCannotMoveVmInUserFolder from a JSON string
storage_drs_cannot_move_vm_in_user_folder_instance = StorageDrsCannotMoveVmInUserFolder.from_json(json)
# print the JSON string representation of the object
print StorageDrsCannotMoveVmInUserFolder.to_json()

# convert the object into a dict
storage_drs_cannot_move_vm_in_user_folder_dict = storage_drs_cannot_move_vm_in_user_folder_instance.to_dict()
# create an instance of StorageDrsCannotMoveVmInUserFolder from a dict
storage_drs_cannot_move_vm_in_user_folder_form_dict = storage_drs_cannot_move_vm_in_user_folder.from_dict(storage_drs_cannot_move_vm_in_user_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


