# ArrayOfEventDescription

A boxed array of *EventDescription*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[EventDescription]**](EventDescription.md) |  | 

## Example

```python
from vmware_vi.models.array_of_event_description import ArrayOfEventDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEventDescription from a JSON string
array_of_event_description_instance = ArrayOfEventDescription.from_json(json)
# print the JSON string representation of the object
print ArrayOfEventDescription.to_json()

# convert the object into a dict
array_of_event_description_dict = array_of_event_description_instance.to_dict()
# create an instance of ArrayOfEventDescription from a dict
array_of_event_description_form_dict = array_of_event_description.from_dict(array_of_event_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


