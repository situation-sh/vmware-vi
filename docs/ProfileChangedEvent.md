# ProfileChangedEvent

This event records that the profile has beed edited  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.profile_changed_event import ProfileChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileChangedEvent from a JSON string
profile_changed_event_instance = ProfileChangedEvent.from_json(json)
# print the JSON string representation of the object
print ProfileChangedEvent.to_json()

# convert the object into a dict
profile_changed_event_dict = profile_changed_event_instance.to_dict()
# create an instance of ProfileChangedEvent from a dict
profile_changed_event_form_dict = profile_changed_event.from_dict(profile_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


