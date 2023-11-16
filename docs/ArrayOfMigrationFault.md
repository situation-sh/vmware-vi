# ArrayOfMigrationFault

A boxed array of *MigrationFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MigrationFault]**](MigrationFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_migration_fault import ArrayOfMigrationFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMigrationFault from a JSON string
array_of_migration_fault_instance = ArrayOfMigrationFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfMigrationFault.to_json()

# convert the object into a dict
array_of_migration_fault_dict = array_of_migration_fault_instance.to_dict()
# create an instance of ArrayOfMigrationFault from a dict
array_of_migration_fault_form_dict = array_of_migration_fault.from_dict(array_of_migration_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


