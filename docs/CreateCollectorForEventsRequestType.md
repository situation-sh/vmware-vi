# CreateCollectorForEventsRequestType

The parameters of *EventManager.CreateCollectorForEvents*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**EventFilterSpec**](EventFilterSpec.md) |  | 

## Example

```python
from vmware_vi.models.create_collector_for_events_request_type import CreateCollectorForEventsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCollectorForEventsRequestType from a JSON string
create_collector_for_events_request_type_instance = CreateCollectorForEventsRequestType.from_json(json)
# print the JSON string representation of the object
print CreateCollectorForEventsRequestType.to_json()

# convert the object into a dict
create_collector_for_events_request_type_dict = create_collector_for_events_request_type_instance.to_dict()
# create an instance of CreateCollectorForEventsRequestType from a dict
create_collector_for_events_request_type_form_dict = create_collector_for_events_request_type.from_dict(create_collector_for_events_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


