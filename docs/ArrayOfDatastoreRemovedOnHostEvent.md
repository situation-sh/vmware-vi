# ArrayOfDatastoreRemovedOnHostEvent

A boxed array of *DatastoreRemovedOnHostEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatastoreRemovedOnHostEvent]**](DatastoreRemovedOnHostEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_datastore_removed_on_host_event import ArrayOfDatastoreRemovedOnHostEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatastoreRemovedOnHostEvent from a JSON string
array_of_datastore_removed_on_host_event_instance = ArrayOfDatastoreRemovedOnHostEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatastoreRemovedOnHostEvent.to_json()

# convert the object into a dict
array_of_datastore_removed_on_host_event_dict = array_of_datastore_removed_on_host_event_instance.to_dict()
# create an instance of ArrayOfDatastoreRemovedOnHostEvent from a dict
array_of_datastore_removed_on_host_event_form_dict = array_of_datastore_removed_on_host_event.from_dict(array_of_datastore_removed_on_host_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


