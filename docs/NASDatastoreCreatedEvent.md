# NASDatastoreCreatedEvent

This event records when a NAS datastore is created. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | 
**datastore_url** | **str** | Url of the associated datastore.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.nas_datastore_created_event import NASDatastoreCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of NASDatastoreCreatedEvent from a JSON string
nas_datastore_created_event_instance = NASDatastoreCreatedEvent.from_json(json)
# print the JSON string representation of the object
print NASDatastoreCreatedEvent.to_json()

# convert the object into a dict
nas_datastore_created_event_dict = nas_datastore_created_event_instance.to_dict()
# create an instance of NASDatastoreCreatedEvent from a dict
nas_datastore_created_event_form_dict = nas_datastore_created_event.from_dict(nas_datastore_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


