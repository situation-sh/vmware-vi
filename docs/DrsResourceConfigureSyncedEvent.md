# DrsResourceConfigureSyncedEvent

This event records when resource configuration specification returns to synchronized from previous failure. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.drs_resource_configure_synced_event import DrsResourceConfigureSyncedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DrsResourceConfigureSyncedEvent from a JSON string
drs_resource_configure_synced_event_instance = DrsResourceConfigureSyncedEvent.from_json(json)
# print the JSON string representation of the object
print DrsResourceConfigureSyncedEvent.to_json()

# convert the object into a dict
drs_resource_configure_synced_event_dict = drs_resource_configure_synced_event_instance.to_dict()
# create an instance of DrsResourceConfigureSyncedEvent from a dict
drs_resource_configure_synced_event_form_dict = drs_resource_configure_synced_event.from_dict(drs_resource_configure_synced_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


