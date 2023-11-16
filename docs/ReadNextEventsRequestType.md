# ReadNextEventsRequestType

The parameters of *EventHistoryCollector.ReadNextEvents*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_count** | **int** | The maximum number of items in the page.  | 

## Example

```python
from vmware_vi.models.read_next_events_request_type import ReadNextEventsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReadNextEventsRequestType from a JSON string
read_next_events_request_type_instance = ReadNextEventsRequestType.from_json(json)
# print the JSON string representation of the object
print ReadNextEventsRequestType.to_json()

# convert the object into a dict
read_next_events_request_type_dict = read_next_events_request_type_instance.to_dict()
# create an instance of ReadNextEventsRequestType from a dict
read_next_events_request_type_form_dict = read_next_events_request_type.from_dict(read_next_events_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


