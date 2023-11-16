# ArrayOfCustomFieldDefAddedEvent

A boxed array of *CustomFieldDefAddedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomFieldDefAddedEvent]**](CustomFieldDefAddedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_custom_field_def_added_event import ArrayOfCustomFieldDefAddedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomFieldDefAddedEvent from a JSON string
array_of_custom_field_def_added_event_instance = ArrayOfCustomFieldDefAddedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomFieldDefAddedEvent.to_json()

# convert the object into a dict
array_of_custom_field_def_added_event_dict = array_of_custom_field_def_added_event_instance.to_dict()
# create an instance of ArrayOfCustomFieldDefAddedEvent from a dict
array_of_custom_field_def_added_event_form_dict = array_of_custom_field_def_added_event.from_dict(array_of_custom_field_def_added_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


