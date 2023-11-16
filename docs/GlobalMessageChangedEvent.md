# GlobalMessageChangedEvent

This event records a change to the global message. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The new message that was set.  | 
**prev_message** | **str** | The previous message that was set.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.global_message_changed_event import GlobalMessageChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalMessageChangedEvent from a JSON string
global_message_changed_event_instance = GlobalMessageChangedEvent.from_json(json)
# print the JSON string representation of the object
print GlobalMessageChangedEvent.to_json()

# convert the object into a dict
global_message_changed_event_dict = global_message_changed_event_instance.to_dict()
# create an instance of GlobalMessageChangedEvent from a dict
global_message_changed_event_form_dict = global_message_changed_event.from_dict(global_message_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


