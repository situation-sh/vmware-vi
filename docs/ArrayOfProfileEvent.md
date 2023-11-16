# ArrayOfProfileEvent

A boxed array of *ProfileEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfileEvent]**](ProfileEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_event import ArrayOfProfileEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfileEvent from a JSON string
array_of_profile_event_instance = ArrayOfProfileEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfileEvent.to_json()

# convert the object into a dict
array_of_profile_event_dict = array_of_profile_event_instance.to_dict()
# create an instance of ArrayOfProfileEvent from a dict
array_of_profile_event_form_dict = array_of_profile_event.from_dict(array_of_profile_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


