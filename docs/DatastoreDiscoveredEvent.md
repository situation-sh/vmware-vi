# DatastoreDiscoveredEvent

This event records when a host is added to VirtualCenter and datastores are discovered. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.datastore_discovered_event import DatastoreDiscoveredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreDiscoveredEvent from a JSON string
datastore_discovered_event_instance = DatastoreDiscoveredEvent.from_json(json)
# print the JSON string representation of the object
print DatastoreDiscoveredEvent.to_json()

# convert the object into a dict
datastore_discovered_event_dict = datastore_discovered_event_instance.to_dict()
# create an instance of DatastoreDiscoveredEvent from a dict
datastore_discovered_event_form_dict = datastore_discovered_event.from_dict(datastore_discovered_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


