# ExtendedEvent

This event is the base class for extended events.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type_id** | **str** | The id of the type of extended event.  ***Since:*** VI API 2.5  | 
**managed_object** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**data** | [**List[ExtendedEventPair]**](ExtendedEventPair.md) | Key/value pairs associated with event.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.extended_event import ExtendedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedEvent from a JSON string
extended_event_instance = ExtendedEvent.from_json(json)
# print the JSON string representation of the object
print ExtendedEvent.to_json()

# convert the object into a dict
extended_event_dict = extended_event_instance.to_dict()
# create an instance of ExtendedEvent from a dict
extended_event_form_dict = extended_event.from_dict(extended_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


