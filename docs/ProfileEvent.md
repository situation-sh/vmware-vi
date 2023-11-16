# ProfileEvent

This event records a Profile specific event.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**ProfileEventArgument**](ProfileEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.profile_event import ProfileEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileEvent from a JSON string
profile_event_instance = ProfileEvent.from_json(json)
# print the JSON string representation of the object
print ProfileEvent.to_json()

# convert the object into a dict
profile_event_dict = profile_event_instance.to_dict()
# create an instance of ProfileEvent from a dict
profile_event_form_dict = profile_event.from_dict(profile_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


