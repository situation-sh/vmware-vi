# PostEventRequestType

The parameters of *EventManager.PostEvent*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_to_post** | [**Event**](Event.md) |  | 
**task_info** | [**TaskInfo**](TaskInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.post_event_request_type import PostEventRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of PostEventRequestType from a JSON string
post_event_request_type_instance = PostEventRequestType.from_json(json)
# print the JSON string representation of the object
print PostEventRequestType.to_json()

# convert the object into a dict
post_event_request_type_dict = post_event_request_type_instance.to_dict()
# create an instance of PostEventRequestType from a dict
post_event_request_type_form_dict = post_event_request_type.from_dict(post_event_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


