# ArrayOfCustomFieldDefEvent

A boxed array of *CustomFieldDefEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomFieldDefEvent]**](CustomFieldDefEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_custom_field_def_event import ArrayOfCustomFieldDefEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomFieldDefEvent from a JSON string
array_of_custom_field_def_event_instance = ArrayOfCustomFieldDefEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomFieldDefEvent.to_json()

# convert the object into a dict
array_of_custom_field_def_event_dict = array_of_custom_field_def_event_instance.to_dict()
# create an instance of ArrayOfCustomFieldDefEvent from a dict
array_of_custom_field_def_event_form_dict = array_of_custom_field_def_event.from_dict(array_of_custom_field_def_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


