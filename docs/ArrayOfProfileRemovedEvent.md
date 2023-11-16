# ArrayOfProfileRemovedEvent

A boxed array of *ProfileRemovedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfileRemovedEvent]**](ProfileRemovedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_removed_event import ArrayOfProfileRemovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfileRemovedEvent from a JSON string
array_of_profile_removed_event_instance = ArrayOfProfileRemovedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfileRemovedEvent.to_json()

# convert the object into a dict
array_of_profile_removed_event_dict = array_of_profile_removed_event_instance.to_dict()
# create an instance of ArrayOfProfileRemovedEvent from a dict
array_of_profile_removed_event_form_dict = array_of_profile_removed_event.from_dict(array_of_profile_removed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


