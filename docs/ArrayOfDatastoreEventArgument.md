# ArrayOfDatastoreEventArgument

A boxed array of *DatastoreEventArgument*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DatastoreEventArgument]**](DatastoreEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.array_of_datastore_event_argument import ArrayOfDatastoreEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDatastoreEventArgument from a JSON string
array_of_datastore_event_argument_instance = ArrayOfDatastoreEventArgument.from_json(json)
# print the JSON string representation of the object
print ArrayOfDatastoreEventArgument.to_json()

# convert the object into a dict
array_of_datastore_event_argument_dict = array_of_datastore_event_argument_instance.to_dict()
# create an instance of ArrayOfDatastoreEventArgument from a dict
array_of_datastore_event_argument_form_dict = array_of_datastore_event_argument.from_dict(array_of_datastore_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


