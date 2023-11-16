# ArrayOfMigrationHostWarningEvent

A boxed array of *MigrationHostWarningEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MigrationHostWarningEvent]**](MigrationHostWarningEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_migration_host_warning_event import ArrayOfMigrationHostWarningEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMigrationHostWarningEvent from a JSON string
array_of_migration_host_warning_event_instance = ArrayOfMigrationHostWarningEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfMigrationHostWarningEvent.to_json()

# convert the object into a dict
array_of_migration_host_warning_event_dict = array_of_migration_host_warning_event_instance.to_dict()
# create an instance of ArrayOfMigrationHostWarningEvent from a dict
array_of_migration_host_warning_event_form_dict = array_of_migration_host_warning_event.from_dict(array_of_migration_host_warning_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


