# DatastoreDuplicatedEvent

This event records when a duplicate datastore name is found.  This event is used in VirtualCenter 1.x and is included for backward compatibility. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.datastore_duplicated_event import DatastoreDuplicatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreDuplicatedEvent from a JSON string
datastore_duplicated_event_instance = DatastoreDuplicatedEvent.from_json(json)
# print the JSON string representation of the object
print DatastoreDuplicatedEvent.to_json()

# convert the object into a dict
datastore_duplicated_event_dict = datastore_duplicated_event_instance.to_dict()
# create an instance of DatastoreDuplicatedEvent from a dict
datastore_duplicated_event_form_dict = datastore_duplicated_event.from_dict(datastore_duplicated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


