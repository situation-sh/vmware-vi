# ArrayOfEventFilterSpecByUsername

A boxed array of *EventFilterSpecByUsername*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[EventFilterSpecByUsername]**](EventFilterSpecByUsername.md) |  | 

## Example

```python
from vmware_vi.models.array_of_event_filter_spec_by_username import ArrayOfEventFilterSpecByUsername

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEventFilterSpecByUsername from a JSON string
array_of_event_filter_spec_by_username_instance = ArrayOfEventFilterSpecByUsername.from_json(json)
# print the JSON string representation of the object
print ArrayOfEventFilterSpecByUsername.to_json()

# convert the object into a dict
array_of_event_filter_spec_by_username_dict = array_of_event_filter_spec_by_username_instance.to_dict()
# create an instance of ArrayOfEventFilterSpecByUsername from a dict
array_of_event_filter_spec_by_username_form_dict = array_of_event_filter_spec_by_username.from_dict(array_of_event_filter_spec_by_username_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


