# ArrayOfMigrationEvent

A boxed array of *MigrationEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MigrationEvent]**](MigrationEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_migration_event import ArrayOfMigrationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMigrationEvent from a JSON string
array_of_migration_event_instance = ArrayOfMigrationEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfMigrationEvent.to_json()

# convert the object into a dict
array_of_migration_event_dict = array_of_migration_event_instance.to_dict()
# create an instance of ArrayOfMigrationEvent from a dict
array_of_migration_event_form_dict = array_of_migration_event.from_dict(array_of_migration_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


