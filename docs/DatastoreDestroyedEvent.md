# DatastoreDestroyedEvent

This event records when a datastore is removed from VirtualCenter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.datastore_destroyed_event import DatastoreDestroyedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreDestroyedEvent from a JSON string
datastore_destroyed_event_instance = DatastoreDestroyedEvent.from_json(json)
# print the JSON string representation of the object
print DatastoreDestroyedEvent.to_json()

# convert the object into a dict
datastore_destroyed_event_dict = datastore_destroyed_event_instance.to_dict()
# create an instance of DatastoreDestroyedEvent from a dict
datastore_destroyed_event_form_dict = datastore_destroyed_event.from_dict(datastore_destroyed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


