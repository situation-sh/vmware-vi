# SessionIsActiveRequestType

The parameters of *SessionManager.SessionIsActive*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session ID to validate.  | 
**user_name** | **str** | User name to validate.  | 

## Example

```python
from vmware_vi.models.session_is_active_request_type import SessionIsActiveRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SessionIsActiveRequestType from a JSON string
session_is_active_request_type_instance = SessionIsActiveRequestType.from_json(json)
# print the JSON string representation of the object
print SessionIsActiveRequestType.to_json()

# convert the object into a dict
session_is_active_request_type_dict = session_is_active_request_type_instance.to_dict()
# create an instance of SessionIsActiveRequestType from a dict
session_is_active_request_type_form_dict = session_is_active_request_type.from_dict(session_is_active_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


