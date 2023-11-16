# DatastoreEventArgument

The event argument is a Datastore object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.datastore_event_argument import DatastoreEventArgument

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreEventArgument from a JSON string
datastore_event_argument_instance = DatastoreEventArgument.from_json(json)
# print the JSON string representation of the object
print DatastoreEventArgument.to_json()

# convert the object into a dict
datastore_event_argument_dict = datastore_event_argument_instance.to_dict()
# create an instance of DatastoreEventArgument from a dict
datastore_event_argument_form_dict = datastore_event_argument.from_dict(datastore_event_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


