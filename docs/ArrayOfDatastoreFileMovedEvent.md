# ArrayOfDatastoreFileMovedEvent

A boxed array of *DatastoreFileMovedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatastoreFileMovedEvent]**](DatastoreFileMovedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_datastore_file_moved_event import ArrayOfDatastoreFileMovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatastoreFileMovedEvent from a JSON string
array_of_datastore_file_moved_event_instance = ArrayOfDatastoreFileMovedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatastoreFileMovedEvent.to_json()

# convert the object into a dict
array_of_datastore_file_moved_event_dict = array_of_datastore_file_moved_event_instance.to_dict()
# create an instance of ArrayOfDatastoreFileMovedEvent from a dict
array_of_datastore_file_moved_event_form_dict = array_of_datastore_file_moved_event.from_dict(array_of_datastore_file_moved_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


