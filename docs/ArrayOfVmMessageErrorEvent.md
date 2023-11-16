# ArrayOfVmMessageErrorEvent

A boxed array of *VmMessageErrorEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmMessageErrorEvent]**](VmMessageErrorEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_message_error_event import ArrayOfVmMessageErrorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmMessageErrorEvent from a JSON string
array_of_vm_message_error_event_instance = ArrayOfVmMessageErrorEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmMessageErrorEvent.to_json()

# convert the object into a dict
array_of_vm_message_error_event_dict = array_of_vm_message_error_event_instance.to_dict()
# create an instance of ArrayOfVmMessageErrorEvent from a dict
array_of_vm_message_error_event_form_dict = array_of_vm_message_error_event.from_dict(array_of_vm_message_error_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


