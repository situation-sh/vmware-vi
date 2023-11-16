# StorageDrsCannotMoveManuallyPlacedVm

This fault is thrown because Storage DRS cannot generate recommendations to relocate a Vm that is placed by user to a specific datastore.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_cannot_move_manually_placed_vm import StorageDrsCannotMoveManuallyPlacedVm

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsCannotMoveManuallyPlacedVm from a JSON string
storage_drs_cannot_move_manually_placed_vm_instance = StorageDrsCannotMoveManuallyPlacedVm.from_json(json)
# print the JSON string representation of the object
print StorageDrsCannotMoveManuallyPlacedVm.to_json()

# convert the object into a dict
storage_drs_cannot_move_manually_placed_vm_dict = storage_drs_cannot_move_manually_placed_vm_instance.to_dict()
# create an instance of StorageDrsCannotMoveManuallyPlacedVm from a dict
storage_drs_cannot_move_manually_placed_vm_form_dict = storage_drs_cannot_move_manually_placed_vm.from_dict(storage_drs_cannot_move_manually_placed_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


