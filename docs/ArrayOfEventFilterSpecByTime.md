# ArrayOfEventFilterSpecByTime

A boxed array of *EventFilterSpecByTime*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[EventFilterSpecByTime]**](EventFilterSpecByTime.md) |  | 

## Example

```python
from vmware_vi.models.array_of_event_filter_spec_by_time import ArrayOfEventFilterSpecByTime

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEventFilterSpecByTime from a JSON string
array_of_event_filter_spec_by_time_instance = ArrayOfEventFilterSpecByTime.from_json(json)
# print the JSON string representation of the object
print ArrayOfEventFilterSpecByTime.to_json()

# convert the object into a dict
array_of_event_filter_spec_by_time_dict = array_of_event_filter_spec_by_time_instance.to_dict()
# create an instance of ArrayOfEventFilterSpecByTime from a dict
array_of_event_filter_spec_by_time_form_dict = array_of_event_filter_spec_by_time.from_dict(array_of_event_filter_spec_by_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


