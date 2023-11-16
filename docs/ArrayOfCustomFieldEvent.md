# ArrayOfCustomFieldEvent

A boxed array of *CustomFieldEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomFieldEvent]**](CustomFieldEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_custom_field_event import ArrayOfCustomFieldEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomFieldEvent from a JSON string
array_of_custom_field_event_instance = ArrayOfCustomFieldEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomFieldEvent.to_json()

# convert the object into a dict
array_of_custom_field_event_dict = array_of_custom_field_event_instance.to_dict()
# create an instance of ArrayOfCustomFieldEvent from a dict
array_of_custom_field_event_form_dict = array_of_custom_field_event.from_dict(array_of_custom_field_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


