# ArrayOfDatastoreFileEvent

A boxed array of *DatastoreFileEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatastoreFileEvent]**](DatastoreFileEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_datastore_file_event import ArrayOfDatastoreFileEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatastoreFileEvent from a JSON string
array_of_datastore_file_event_instance = ArrayOfDatastoreFileEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatastoreFileEvent.to_json()

# convert the object into a dict
array_of_datastore_file_event_dict = array_of_datastore_file_event_instance.to_dict()
# create an instance of ArrayOfDatastoreFileEvent from a dict
array_of_datastore_file_event_form_dict = array_of_datastore_file_event.from_dict(array_of_datastore_file_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


