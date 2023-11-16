# CanceledHostOperationEvent

An operation performed on the host was canceled.  Typically, a previous event in the sequence of events contains more information about the cause of this cancellation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.canceled_host_operation_event import CanceledHostOperationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CanceledHostOperationEvent from a JSON string
canceled_host_operation_event_instance = CanceledHostOperationEvent.from_json(json)
# print the JSON string representation of the object
print CanceledHostOperationEvent.to_json()

# convert the object into a dict
canceled_host_operation_event_dict = canceled_host_operation_event_instance.to_dict()
# create an instance of CanceledHostOperationEvent from a dict
canceled_host_operation_event_form_dict = canceled_host_operation_event.from_dict(canceled_host_operation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


