# LocalDatastoreCreatedEvent

This event records when a local datastore is created. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | 
**datastore_url** | **str** | Url of the associated datastore.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.local_datastore_created_event import LocalDatastoreCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LocalDatastoreCreatedEvent from a JSON string
local_datastore_created_event_instance = LocalDatastoreCreatedEvent.from_json(json)
# print the JSON string representation of the object
print LocalDatastoreCreatedEvent.to_json()

# convert the object into a dict
local_datastore_created_event_dict = local_datastore_created_event_instance.to_dict()
# create an instance of LocalDatastoreCreatedEvent from a dict
local_datastore_created_event_form_dict = local_datastore_created_event.from_dict(local_datastore_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


