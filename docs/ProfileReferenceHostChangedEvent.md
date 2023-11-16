# ProfileReferenceHostChangedEvent

This event records that the reference host associated with this profile has changed  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**reference_host_name** | **str** | The newly associated reference host name  ***Since:*** vSphere API 6.5  | [optional] 
**prev_reference_host_name** | **str** | The previous reference host name  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.profile_reference_host_changed_event import ProfileReferenceHostChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileReferenceHostChangedEvent from a JSON string
profile_reference_host_changed_event_instance = ProfileReferenceHostChangedEvent.from_json(json)
# print the JSON string representation of the object
print ProfileReferenceHostChangedEvent.to_json()

# convert the object into a dict
profile_reference_host_changed_event_dict = profile_reference_host_changed_event_instance.to_dict()
# create an instance of ProfileReferenceHostChangedEvent from a dict
profile_reference_host_changed_event_form_dict = profile_reference_host_changed_event.from_dict(profile_reference_host_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


