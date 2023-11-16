# ArrayOfInvalidEvent

A boxed array of *InvalidEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidEvent]**](InvalidEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_event import ArrayOfInvalidEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidEvent from a JSON string
array_of_invalid_event_instance = ArrayOfInvalidEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidEvent.to_json()

# convert the object into a dict
array_of_invalid_event_dict = array_of_invalid_event_instance.to_dict()
# create an instance of ArrayOfInvalidEvent from a dict
array_of_invalid_event_form_dict = array_of_invalid_event.from_dict(array_of_invalid_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


