# DatastoreEvent

These are datastore events. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.datastore_event import DatastoreEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreEvent from a JSON string
datastore_event_instance = DatastoreEvent.from_json(json)
# print the JSON string representation of the object
print DatastoreEvent.to_json()

# convert the object into a dict
datastore_event_dict = datastore_event_instance.to_dict()
# create an instance of DatastoreEvent from a dict
datastore_event_form_dict = datastore_event.from_dict(datastore_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


