# ArrayOfDatastoreDiscoveredEvent

A boxed array of *DatastoreDiscoveredEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatastoreDiscoveredEvent]**](DatastoreDiscoveredEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_datastore_discovered_event import ArrayOfDatastoreDiscoveredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatastoreDiscoveredEvent from a JSON string
array_of_datastore_discovered_event_instance = ArrayOfDatastoreDiscoveredEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatastoreDiscoveredEvent.to_json()

# convert the object into a dict
array_of_datastore_discovered_event_dict = array_of_datastore_discovered_event_instance.to_dict()
# create an instance of ArrayOfDatastoreDiscoveredEvent from a dict
array_of_datastore_discovered_event_form_dict = array_of_datastore_discovered_event.from_dict(array_of_datastore_discovered_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


