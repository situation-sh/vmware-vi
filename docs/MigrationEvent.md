# MigrationEvent

These are events used to describe migration warning and errors 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.migration_event import MigrationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationEvent from a JSON string
migration_event_instance = MigrationEvent.from_json(json)
# print the JSON string representation of the object
print MigrationEvent.to_json()

# convert the object into a dict
migration_event_dict = migration_event_instance.to_dict()
# create an instance of MigrationEvent from a dict
migration_event_form_dict = migration_event.from_dict(migration_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


