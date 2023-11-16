# ArrayOfProfileDissociatedEvent

A boxed array of *ProfileDissociatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfileDissociatedEvent]**](ProfileDissociatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_dissociated_event import ArrayOfProfileDissociatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfileDissociatedEvent from a JSON string
array_of_profile_dissociated_event_instance = ArrayOfProfileDissociatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfileDissociatedEvent.to_json()

# convert the object into a dict
array_of_profile_dissociated_event_dict = array_of_profile_dissociated_event_instance.to_dict()
# create an instance of ArrayOfProfileDissociatedEvent from a dict
array_of_profile_dissociated_event_form_dict = array_of_profile_dissociated_event.from_dict(array_of_profile_dissociated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


