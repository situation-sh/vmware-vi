# ArrayOfGeneralUserEvent

A boxed array of *GeneralUserEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GeneralUserEvent]**](GeneralUserEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_general_user_event import ArrayOfGeneralUserEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGeneralUserEvent from a JSON string
array_of_general_user_event_instance = ArrayOfGeneralUserEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfGeneralUserEvent.to_json()

# convert the object into a dict
array_of_general_user_event_dict = array_of_general_user_event_instance.to_dict()
# create an instance of ArrayOfGeneralUserEvent from a dict
array_of_general_user_event_form_dict = array_of_general_user_event.from_dict(array_of_general_user_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


