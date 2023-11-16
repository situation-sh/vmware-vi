# ArrayOfLocalDatastoreCreatedEvent

A boxed array of *LocalDatastoreCreatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LocalDatastoreCreatedEvent]**](LocalDatastoreCreatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_local_datastore_created_event import ArrayOfLocalDatastoreCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLocalDatastoreCreatedEvent from a JSON string
array_of_local_datastore_created_event_instance = ArrayOfLocalDatastoreCreatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfLocalDatastoreCreatedEvent.to_json()

# convert the object into a dict
array_of_local_datastore_created_event_dict = array_of_local_datastore_created_event_instance.to_dict()
# create an instance of ArrayOfLocalDatastoreCreatedEvent from a dict
array_of_local_datastore_created_event_form_dict = array_of_local_datastore_created_event.from_dict(array_of_local_datastore_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


