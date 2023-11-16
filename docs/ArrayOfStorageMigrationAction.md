# ArrayOfStorageMigrationAction

A boxed array of *StorageMigrationAction*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StorageMigrationAction]**](StorageMigrationAction.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_migration_action import ArrayOfStorageMigrationAction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStorageMigrationAction from a JSON string
array_of_storage_migration_action_instance = ArrayOfStorageMigrationAction.from_json(json)
# print the JSON string representation of the object
print ArrayOfStorageMigrationAction.to_json()

# convert the object into a dict
array_of_storage_migration_action_dict = array_of_storage_migration_action_instance.to_dict()
# create an instance of ArrayOfStorageMigrationAction from a dict
array_of_storage_migration_action_form_dict = array_of_storage_migration_action.from_dict(array_of_storage_migration_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


