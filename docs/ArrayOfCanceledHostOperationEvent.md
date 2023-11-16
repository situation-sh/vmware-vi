# ArrayOfCanceledHostOperationEvent

A boxed array of *CanceledHostOperationEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CanceledHostOperationEvent]**](CanceledHostOperationEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_canceled_host_operation_event import ArrayOfCanceledHostOperationEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCanceledHostOperationEvent from a JSON string
array_of_canceled_host_operation_event_instance = ArrayOfCanceledHostOperationEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfCanceledHostOperationEvent.to_json()

# convert the object into a dict
array_of_canceled_host_operation_event_dict = array_of_canceled_host_operation_event_instance.to_dict()
# create an instance of ArrayOfCanceledHostOperationEvent from a dict
array_of_canceled_host_operation_event_form_dict = array_of_canceled_host_operation_event.from_dict(array_of_canceled_host_operation_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


