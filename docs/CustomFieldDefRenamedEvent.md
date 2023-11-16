# CustomFieldDefRenamedEvent

This event records the renaming of a custom field definition. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_name** | **str** |  | 

## Example

```python
from vmware_vi.models.custom_field_def_renamed_event import CustomFieldDefRenamedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldDefRenamedEvent from a JSON string
custom_field_def_renamed_event_instance = CustomFieldDefRenamedEvent.from_json(json)
# print the JSON string representation of the object
print CustomFieldDefRenamedEvent.to_json()

# convert the object into a dict
custom_field_def_renamed_event_dict = custom_field_def_renamed_event_instance.to_dict()
# create an instance of CustomFieldDefRenamedEvent from a dict
custom_field_def_renamed_event_form_dict = custom_field_def_renamed_event.from_dict(custom_field_def_renamed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


