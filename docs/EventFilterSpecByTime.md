# EventFilterSpecByTime

This option specifies a time range used to filter event history. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin_time** | **datetime** | The beginning of the time range.  If this property is not set, then events are collected from the earliest time in the database.  | [optional] 
**end_time** | **datetime** | The end of the time range.  If this property is not specified, then events are collected up to the latest time in the database.  | [optional] 

## Example

```python
from vmware_vi.models.event_filter_spec_by_time import EventFilterSpecByTime

# TODO update the JSON string below
json = "{}"
# create an instance of EventFilterSpecByTime from a JSON string
event_filter_spec_by_time_instance = EventFilterSpecByTime.from_json(json)
# print the JSON string representation of the object
print EventFilterSpecByTime.to_json()

# convert the object into a dict
event_filter_spec_by_time_dict = event_filter_spec_by_time_instance.to_dict()
# create an instance of EventFilterSpecByTime from a dict
event_filter_spec_by_time_form_dict = event_filter_spec_by_time.from_dict(event_filter_spec_by_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


