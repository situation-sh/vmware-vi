# ArrayOfDatastoreRenamedEvent

A boxed array of *DatastoreRenamedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatastoreRenamedEvent]**](DatastoreRenamedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_datastore_renamed_event import ArrayOfDatastoreRenamedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatastoreRenamedEvent from a JSON string
array_of_datastore_renamed_event_instance = ArrayOfDatastoreRenamedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatastoreRenamedEvent.to_json()

# convert the object into a dict
array_of_datastore_renamed_event_dict = array_of_datastore_renamed_event_instance.to_dict()
# create an instance of ArrayOfDatastoreRenamedEvent from a dict
array_of_datastore_renamed_event_form_dict = array_of_datastore_renamed_event.from_dict(array_of_datastore_renamed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


