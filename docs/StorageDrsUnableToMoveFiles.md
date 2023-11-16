# StorageDrsUnableToMoveFiles

This fault is thrown when Storage DRS cannot generate recommendations to move VM files due to pre-existing cross datastore disk backings.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.storage_drs_unable_to_move_files import StorageDrsUnableToMoveFiles

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDrsUnableToMoveFiles from a JSON string
storage_drs_unable_to_move_files_instance = StorageDrsUnableToMoveFiles.from_json(json)
# print the JSON string representation of the object
print StorageDrsUnableToMoveFiles.to_json()

# convert the object into a dict
storage_drs_unable_to_move_files_dict = storage_drs_unable_to_move_files_instance.to_dict()
# create an instance of StorageDrsUnableToMoveFiles from a dict
storage_drs_unable_to_move_files_form_dict = storage_drs_unable_to_move_files.from_dict(storage_drs_unable_to_move_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


