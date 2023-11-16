# MigrationHostWarningEvent

A migration warning that includes the destination host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dst_host** | [**HostEventArgument**](HostEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.migration_host_warning_event import MigrationHostWarningEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationHostWarningEvent from a JSON string
migration_host_warning_event_instance = MigrationHostWarningEvent.from_json(json)
# print the JSON string representation of the object
print MigrationHostWarningEvent.to_json()

# convert the object into a dict
migration_host_warning_event_dict = migration_host_warning_event_instance.to_dict()
# create an instance of MigrationHostWarningEvent from a dict
migration_host_warning_event_form_dict = migration_host_warning_event.from_dict(migration_host_warning_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


