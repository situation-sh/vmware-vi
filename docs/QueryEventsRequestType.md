# QueryEventsRequestType

The parameters of *EventManager.QueryEvents*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**EventFilterSpec**](EventFilterSpec.md) |  | 

## Example

```python
from vmware_vi.models.query_events_request_type import QueryEventsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryEventsRequestType from a JSON string
query_events_request_type_instance = QueryEventsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryEventsRequestType.to_json()

# convert the object into a dict
query_events_request_type_dict = query_events_request_type_instance.to_dict()
# create an instance of QueryEventsRequestType from a dict
query_events_request_type_form_dict = query_events_request_type.from_dict(query_events_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


