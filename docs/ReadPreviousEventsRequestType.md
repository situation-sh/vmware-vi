# ReadPreviousEventsRequestType

The parameters of *EventHistoryCollector.ReadPreviousEvents*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_count** | **int** | The maximum number of items in the page.  | 

## Example

```python
from vmware_vi.models.read_previous_events_request_type import ReadPreviousEventsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReadPreviousEventsRequestType from a JSON string
read_previous_events_request_type_instance = ReadPreviousEventsRequestType.from_json(json)
# print the JSON string representation of the object
print ReadPreviousEventsRequestType.to_json()

# convert the object into a dict
read_previous_events_request_type_dict = read_previous_events_request_type_instance.to_dict()
# create an instance of ReadPreviousEventsRequestType from a dict
read_previous_events_request_type_form_dict = read_previous_events_request_type.from_dict(read_previous_events_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


