# ArrayOfMigrationErrorEvent

A boxed array of *MigrationErrorEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MigrationErrorEvent]**](MigrationErrorEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_migration_error_event import ArrayOfMigrationErrorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMigrationErrorEvent from a JSON string
array_of_migration_error_event_instance = ArrayOfMigrationErrorEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfMigrationErrorEvent.to_json()

# convert the object into a dict
array_of_migration_error_event_dict = array_of_migration_error_event_instance.to_dict()
# create an instance of ArrayOfMigrationErrorEvent from a dict
array_of_migration_error_event_form_dict = array_of_migration_error_event.from_dict(array_of_migration_error_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


