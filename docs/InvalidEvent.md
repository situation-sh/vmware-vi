# InvalidEvent

A InvalidEvent fault is thrown when the event is malformed.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_event import InvalidEvent

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidEvent from a JSON string
invalid_event_instance = InvalidEvent.from_json(json)
# print the JSON string representation of the object
print InvalidEvent.to_json()

# convert the object into a dict
invalid_event_dict = invalid_event_instance.to_dict()
# create an instance of InvalidEvent from a dict
invalid_event_form_dict = invalid_event.from_dict(invalid_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


