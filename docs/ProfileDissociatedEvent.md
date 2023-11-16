# ProfileDissociatedEvent

This event records that a Profile was dissociated from a managed entity  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.profile_dissociated_event import ProfileDissociatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileDissociatedEvent from a JSON string
profile_dissociated_event_instance = ProfileDissociatedEvent.from_json(json)
# print the JSON string representation of the object
print ProfileDissociatedEvent.to_json()

# convert the object into a dict
profile_dissociated_event_dict = profile_dissociated_event_instance.to_dict()
# create an instance of ProfileDissociatedEvent from a dict
profile_dissociated_event_form_dict = profile_dissociated_event.from_dict(profile_dissociated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


