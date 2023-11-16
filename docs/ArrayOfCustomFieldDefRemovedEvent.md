# ArrayOfCustomFieldDefRemovedEvent

A boxed array of *CustomFieldDefRemovedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomFieldDefRemovedEvent]**](CustomFieldDefRemovedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_custom_field_def_removed_event import ArrayOfCustomFieldDefRemovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomFieldDefRemovedEvent from a JSON string
array_of_custom_field_def_removed_event_instance = ArrayOfCustomFieldDefRemovedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomFieldDefRemovedEvent.to_json()

# convert the object into a dict
array_of_custom_field_def_removed_event_dict = array_of_custom_field_def_removed_event_instance.to_dict()
# create an instance of ArrayOfCustomFieldDefRemovedEvent from a dict
array_of_custom_field_def_removed_event_form_dict = array_of_custom_field_def_removed_event.from_dict(array_of_custom_field_def_removed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


