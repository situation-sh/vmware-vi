# ProfileAssociatedEvent

This event records that a Profile was associated with a managed entitiy.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.profile_associated_event import ProfileAssociatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileAssociatedEvent from a JSON string
profile_associated_event_instance = ProfileAssociatedEvent.from_json(json)
# print the JSON string representation of the object
print ProfileAssociatedEvent.to_json()

# convert the object into a dict
profile_associated_event_dict = profile_associated_event_instance.to_dict()
# create an instance of ProfileAssociatedEvent from a dict
profile_associated_event_form_dict = profile_associated_event.from_dict(profile_associated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


