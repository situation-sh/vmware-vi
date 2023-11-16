# ArrayOfTimedOutHostOperationEvent

A boxed array of *TimedOutHostOperationEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TimedOutHostOperationEvent]**](TimedOutHostOperationEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_timed_out_host_operation_event import ArrayOfTimedOutHostOperationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTimedOutHostOperationEvent from a JSON string
array_of_timed_out_host_operation_event_instance = ArrayOfTimedOutHostOperationEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfTimedOutHostOperationEvent.to_json()

# convert the object into a dict
array_of_timed_out_host_operation_event_dict = array_of_timed_out_host_operation_event_instance.to_dict()
# create an instance of ArrayOfTimedOutHostOperationEvent from a dict
array_of_timed_out_host_operation_event_form_dict = array_of_timed_out_host_operation_event.from_dict(array_of_timed_out_host_operation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


