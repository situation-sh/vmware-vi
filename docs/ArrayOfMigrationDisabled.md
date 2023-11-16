# ArrayOfMigrationDisabled

A boxed array of *MigrationDisabled*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MigrationDisabled]**](MigrationDisabled.md) |  | 

## Example

```python
from vmware_vi.models.array_of_migration_disabled import ArrayOfMigrationDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMigrationDisabled from a JSON string
array_of_migration_disabled_instance = ArrayOfMigrationDisabled.from_json(json)
# print the JSON string representation of the object
print ArrayOfMigrationDisabled.to_json()

# convert the object into a dict
array_of_migration_disabled_dict = array_of_migration_disabled_instance.to_dict()
# create an instance of ArrayOfMigrationDisabled from a dict
array_of_migration_disabled_form_dict = array_of_migration_disabled.from_dict(array_of_migration_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


