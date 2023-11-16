# CustomFieldEvent

These are custom field events. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.custom_field_event import CustomFieldEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldEvent from a JSON string
custom_field_event_instance = CustomFieldEvent.from_json(json)
# print the JSON string representation of the object
print CustomFieldEvent.to_json()

# convert the object into a dict
custom_field_event_dict = custom_field_event_instance.to_dict()
# create an instance of CustomFieldEvent from a dict
custom_field_event_form_dict = custom_field_event.from_dict(custom_field_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


