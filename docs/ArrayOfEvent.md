# ArrayOfEvent

A boxed array of *Event*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Event]**](Event.md) |  | 

## Example

```python
from vmware_vi.models.array_of_event import ArrayOfEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEvent from a JSON string
array_of_event_instance = ArrayOfEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfEvent.to_json()

# convert the object into a dict
array_of_event_dict = array_of_event_instance.to_dict()
# create an instance of ArrayOfEvent from a dict
array_of_event_form_dict = array_of_event.from_dict(array_of_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


