# ArrayOfCustomFieldValueChangedEvent

A boxed array of *CustomFieldValueChangedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomFieldValueChangedEvent]**](CustomFieldValueChangedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_custom_field_value_changed_event import ArrayOfCustomFieldValueChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomFieldValueChangedEvent from a JSON string
array_of_custom_field_value_changed_event_instance = ArrayOfCustomFieldValueChangedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomFieldValueChangedEvent.to_json()

# convert the object into a dict
array_of_custom_field_value_changed_event_dict = array_of_custom_field_value_changed_event_instance.to_dict()
# create an instance of ArrayOfCustomFieldValueChangedEvent from a dict
array_of_custom_field_value_changed_event_form_dict = array_of_custom_field_value_changed_event.from_dict(array_of_custom_field_value_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


