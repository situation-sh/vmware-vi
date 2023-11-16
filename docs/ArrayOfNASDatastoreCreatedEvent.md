# ArrayOfNASDatastoreCreatedEvent

A boxed array of *NASDatastoreCreatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NASDatastoreCreatedEvent]**](NASDatastoreCreatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_nas_datastore_created_event import ArrayOfNASDatastoreCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNASDatastoreCreatedEvent from a JSON string
array_of_nas_datastore_created_event_instance = ArrayOfNASDatastoreCreatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfNASDatastoreCreatedEvent.to_json()

# convert the object into a dict
array_of_nas_datastore_created_event_dict = array_of_nas_datastore_created_event_instance.to_dict()
# create an instance of ArrayOfNASDatastoreCreatedEvent from a dict
array_of_nas_datastore_created_event_form_dict = array_of_nas_datastore_created_event.from_dict(array_of_nas_datastore_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


