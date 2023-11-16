# SessionTerminatedEvent

This event records the termination of a session. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | The unique identifier of the terminated session.  | 
**terminated_username** | **str** | The name of the user owning the terminated session.  | 

## Example

```python
from vmware_vi.models.session_terminated_event import SessionTerminatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SessionTerminatedEvent from a JSON string
session_terminated_event_instance = SessionTerminatedEvent.from_json(json)
# print the JSON string representation of the object
print SessionTerminatedEvent.to_json()

# convert the object into a dict
session_terminated_event_dict = session_terminated_event_instance.to_dict()
# create an instance of SessionTerminatedEvent from a dict
session_terminated_event_form_dict = session_terminated_event.from_dict(session_terminated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


