# ArrayOfDatastoreEvent

A boxed array of *DatastoreEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatastoreEvent]**](DatastoreEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_datastore_event import ArrayOfDatastoreEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatastoreEvent from a JSON string
array_of_datastore_event_instance = ArrayOfDatastoreEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatastoreEvent.to_json()

# convert the object into a dict
array_of_datastore_event_dict = array_of_datastore_event_instance.to_dict()
# create an instance of ArrayOfDatastoreEvent from a dict
array_of_datastore_event_form_dict = array_of_datastore_event.from_dict(array_of_datastore_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


