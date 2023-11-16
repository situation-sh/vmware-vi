# AlreadyAuthenticatedSessionEvent

This event records a failed user logon due to the user already being logged on. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.already_authenticated_session_event import AlreadyAuthenticatedSessionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AlreadyAuthenticatedSessionEvent from a JSON string
already_authenticated_session_event_instance = AlreadyAuthenticatedSessionEvent.from_json(json)
# print the JSON string representation of the object
print AlreadyAuthenticatedSessionEvent.to_json()

# convert the object into a dict
already_authenticated_session_event_dict = already_authenticated_session_event_instance.to_dict()
# create an instance of AlreadyAuthenticatedSessionEvent from a dict
already_authenticated_session_event_form_dict = already_authenticated_session_event.from_dict(already_authenticated_session_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


