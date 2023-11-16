# ArrayOfMigrationResourceWarningEvent

A boxed array of *MigrationResourceWarningEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MigrationResourceWarningEvent]**](MigrationResourceWarningEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_migration_resource_warning_event import ArrayOfMigrationResourceWarningEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMigrationResourceWarningEvent from a JSON string
array_of_migration_resource_warning_event_instance = ArrayOfMigrationResourceWarningEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfMigrationResourceWarningEvent.to_json()

# convert the object into a dict
array_of_migration_resource_warning_event_dict = array_of_migration_resource_warning_event_instance.to_dict()
# create an instance of ArrayOfMigrationResourceWarningEvent from a dict
array_of_migration_resource_warning_event_form_dict = array_of_migration_resource_warning_event.from_dict(array_of_migration_resource_warning_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


