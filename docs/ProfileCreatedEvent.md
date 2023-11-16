# ProfileCreatedEvent

This event records that a Profile was created.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.profile_created_event import ProfileCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileCreatedEvent from a JSON string
profile_created_event_instance = ProfileCreatedEvent.from_json(json)
# print the JSON string representation of the object
print ProfileCreatedEvent.to_json()

# convert the object into a dict
profile_created_event_dict = profile_created_event_instance.to_dict()
# create an instance of ProfileCreatedEvent from a dict
profile_created_event_form_dict = profile_created_event.from_dict(profile_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


