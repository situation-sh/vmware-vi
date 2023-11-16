# ArrayOfProfileAssociatedEvent

A boxed array of *ProfileAssociatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ProfileAssociatedEvent]**](ProfileAssociatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_profile_associated_event import ArrayOfProfileAssociatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfProfileAssociatedEvent from a JSON string
array_of_profile_associated_event_instance = ArrayOfProfileAssociatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfProfileAssociatedEvent.to_json()

# convert the object into a dict
array_of_profile_associated_event_dict = array_of_profile_associated_event_instance.to_dict()
# create an instance of ArrayOfProfileAssociatedEvent from a dict
array_of_profile_associated_event_form_dict = array_of_profile_associated_event.from_dict(array_of_profile_associated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


