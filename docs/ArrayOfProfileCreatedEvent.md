# ArrayOfProfileCreatedEvent

A boxed array of *ProfileCreatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfileCreatedEvent]**](ProfileCreatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_created_event import ArrayOfProfileCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfileCreatedEvent from a JSON string
array_of_profile_created_event_instance = ArrayOfProfileCreatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfileCreatedEvent.to_json()

# convert the object into a dict
array_of_profile_created_event_dict = array_of_profile_created_event_instance.to_dict()
# create an instance of ArrayOfProfileCreatedEvent from a dict
array_of_profile_created_event_form_dict = array_of_profile_created_event.from_dict(array_of_profile_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


