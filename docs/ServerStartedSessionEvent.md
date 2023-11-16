# ServerStartedSessionEvent

This event records the starting of the VirtualCenter server. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.server_started_session_event import ServerStartedSessionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ServerStartedSessionEvent from a JSON string
server_started_session_event_instance = ServerStartedSessionEvent.from_json(json)
# print the JSON string representation of the object
print ServerStartedSessionEvent.to_json()

# convert the object into a dict
server_started_session_event_dict = server_started_session_event_instance.to_dict()
# create an instance of ServerStartedSessionEvent from a dict
server_started_session_event_form_dict = server_started_session_event.from_dict(server_started_session_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


