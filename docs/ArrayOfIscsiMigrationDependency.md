# ArrayOfIscsiMigrationDependency

A boxed array of *IscsiMigrationDependency*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IscsiMigrationDependency]**](IscsiMigrationDependency.md) |  | 

## Example

```python
from vmware_vi.models.array_of_iscsi_migration_dependency import ArrayOfIscsiMigrationDependency

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIscsiMigrationDependency from a JSON string
array_of_iscsi_migration_dependency_instance = ArrayOfIscsiMigrationDependency.from_json(json)
# print the JSON string representation of the object
print ArrayOfIscsiMigrationDependency.to_json()

# convert the object into a dict
array_of_iscsi_migration_dependency_dict = array_of_iscsi_migration_dependency_instance.to_dict()
# create an instance of ArrayOfIscsiMigrationDependency from a dict
array_of_iscsi_migration_dependency_form_dict = array_of_iscsi_migration_dependency.from_dict(array_of_iscsi_migration_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


