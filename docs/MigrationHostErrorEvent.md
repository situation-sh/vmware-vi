# MigrationHostErrorEvent

A migration error that includes the destination host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dst_host** | [**HostEventArgument**](HostEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.migration_host_error_event import MigrationHostErrorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationHostErrorEvent from a JSON string
migration_host_error_event_instance = MigrationHostErrorEvent.from_json(json)
# print the JSON string representation of the object
print MigrationHostErrorEvent.to_json()

# convert the object into a dict
migration_host_error_event_dict = migration_host_error_event_instance.to_dict()
# create an instance of MigrationHostErrorEvent from a dict
migration_host_error_event_form_dict = migration_host_error_event.from_dict(migration_host_error_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


