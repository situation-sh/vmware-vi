# LogUserEventRequestType

The parameters of *EventManager.LogUserEvent*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**msg** | **str** | The message to be logged.  | 

## Example

```python
from vmware_vi.models.log_user_event_request_type import LogUserEventRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of LogUserEventRequestType from a JSON string
log_user_event_request_type_instance = LogUserEventRequestType.from_json(json)
# print the JSON string representation of the object
print LogUserEventRequestType.to_json()

# convert the object into a dict
log_user_event_request_type_dict = log_user_event_request_type_instance.to_dict()
# create an instance of LogUserEventRequestType from a dict
log_user_event_request_type_form_dict = log_user_event_request_type.from_dict(log_user_event_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


