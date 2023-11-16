# GeneralUserEvent

This event is the general user event type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ManagedEntityEventArgument**](ManagedEntityEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.general_user_event import GeneralUserEvent

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralUserEvent from a JSON string
general_user_event_instance = GeneralUserEvent.from_json(json)
# print the JSON string representation of the object
print GeneralUserEvent.to_json()

# convert the object into a dict
general_user_event_dict = general_user_event_instance.to_dict()
# create an instance of GeneralUserEvent from a dict
general_user_event_form_dict = general_user_event.from_dict(general_user_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


