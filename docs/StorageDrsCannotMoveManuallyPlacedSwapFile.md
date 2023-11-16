# StorageDrsCannotMoveManuallyPlacedSwapFile

This fault is thrown because Storage DRS cannot generate recommendations to relocate VM because it has a manually selected fixed location for its swap file.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_cannot_move_manually_placed_swap_file import StorageDrsCannotMoveManuallyPlacedSwapFile

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsCannotMoveManuallyPlacedSwapFile from a JSON string
storage_drs_cannot_move_manually_placed_swap_file_instance = StorageDrsCannotMoveManuallyPlacedSwapFile.from_json(json)
# print the JSON string representation of the object
print StorageDrsCannotMoveManuallyPlacedSwapFile.to_json()

# convert the object into a dict
storage_drs_cannot_move_manually_placed_swap_file_dict = storage_drs_cannot_move_manually_placed_swap_file_instance.to_dict()
# create an instance of StorageDrsCannotMoveManuallyPlacedSwapFile from a dict
storage_drs_cannot_move_manually_placed_swap_file_form_dict = storage_drs_cannot_move_manually_placed_swap_file.from_dict(storage_drs_cannot_move_manually_placed_swap_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


