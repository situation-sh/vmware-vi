# CloneSessionRequestType

The parameters of *SessionManager.CloneSession*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clone_ticket** | **str** | ticket string acquired via *SessionManager.AcquireCloneTicket*.  | 

## Example

```python
from vmware_vi.models.clone_session_request_type import CloneSessionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CloneSessionRequestType from a JSON string
clone_session_request_type_instance = CloneSessionRequestType.from_json(json)
# print the JSON string representation of the object
print CloneSessionRequestType.to_json()

# convert the object into a dict
clone_session_request_type_dict = clone_session_request_type_instance.to_dict()
# create an instance of CloneSessionRequestType from a dict
clone_session_request_type_form_dict = clone_session_request_type.from_dict(clone_session_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


