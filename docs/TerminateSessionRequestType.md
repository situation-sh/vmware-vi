# TerminateSessionRequestType

The parameters of *SessionManager.TerminateSession*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **List[str]** | A list of sessions to terminate.  | 

## Example

```python
from vmware_vi.models.terminate_session_request_type import TerminateSessionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of TerminateSessionRequestType from a JSON string
terminate_session_request_type_instance = TerminateSessionRequestType.from_json(json)
# print the JSON string representation of the object
print TerminateSessionRequestType.to_json()

# convert the object into a dict
terminate_session_request_type_dict = terminate_session_request_type_instance.to_dict()
# create an instance of TerminateSessionRequestType from a dict
terminate_session_request_type_form_dict = terminate_session_request_type.from_dict(terminate_session_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


