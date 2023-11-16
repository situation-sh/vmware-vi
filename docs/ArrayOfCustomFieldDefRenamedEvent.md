# ArrayOfCustomFieldDefRenamedEvent

A boxed array of *CustomFieldDefRenamedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomFieldDefRenamedEvent]**](CustomFieldDefRenamedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_custom_field_def_renamed_event import ArrayOfCustomFieldDefRenamedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomFieldDefRenamedEvent from a JSON string
array_of_custom_field_def_renamed_event_instance = ArrayOfCustomFieldDefRenamedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomFieldDefRenamedEvent.to_json()

# convert the object into a dict
array_of_custom_field_def_renamed_event_dict = array_of_custom_field_def_renamed_event_instance.to_dict()
# create an instance of ArrayOfCustomFieldDefRenamedEvent from a dict
array_of_custom_field_def_renamed_event_form_dict = array_of_custom_field_def_renamed_event.from_dict(array_of_custom_field_def_renamed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


