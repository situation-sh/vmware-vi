# TimedOutHostOperationEvent

This event indicates that an operation performed on the host timed out.  Typically, a previous event in the sequence of events contains more information about the cause of the operation timing out. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.timed_out_host_operation_event import TimedOutHostOperationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TimedOutHostOperationEvent from a JSON string
timed_out_host_operation_event_instance = TimedOutHostOperationEvent.from_json(json)
# print the JSON string representation of the object
print TimedOutHostOperationEvent.to_json()

# convert the object into a dict
timed_out_host_operation_event_dict = timed_out_host_operation_event_instance.to_dict()
# create an instance of TimedOutHostOperationEvent from a dict
timed_out_host_operation_event_form_dict = timed_out_host_operation_event.from_dict(timed_out_host_operation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


