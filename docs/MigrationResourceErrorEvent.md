# MigrationResourceErrorEvent

A migration error that includes both the destination host and resource pool. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dst_pool** | [**ResourcePoolEventArgument**](ResourcePoolEventArgument.md) |  | 
**dst_host** | [**HostEventArgument**](HostEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.migration_resource_error_event import MigrationResourceErrorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationResourceErrorEvent from a JSON string
migration_resource_error_event_instance = MigrationResourceErrorEvent.from_json(json)
# print the JSON string representation of the object
print MigrationResourceErrorEvent.to_json()

# convert the object into a dict
migration_resource_error_event_dict = migration_resource_error_event_instance.to_dict()
# create an instance of MigrationResourceErrorEvent from a dict
migration_resource_error_event_form_dict = migration_resource_error_event.from_dict(migration_resource_error_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


