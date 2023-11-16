# DatastoreRemovedOnHostEvent

This event records when a datastore is removed from a host but not from VirtualCenter. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.datastore_removed_on_host_event import DatastoreRemovedOnHostEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreRemovedOnHostEvent from a JSON string
datastore_removed_on_host_event_instance = DatastoreRemovedOnHostEvent.from_json(json)
# print the JSON string representation of the object
print DatastoreRemovedOnHostEvent.to_json()

# convert the object into a dict
datastore_removed_on_host_event_dict = datastore_removed_on_host_event_instance.to_dict()
# create an instance of DatastoreRemovedOnHostEvent from a dict
datastore_removed_on_host_event_form_dict = datastore_removed_on_host_event.from_dict(datastore_removed_on_host_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


