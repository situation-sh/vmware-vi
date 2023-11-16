# ArrayOfVmMessageWarningEvent

A boxed array of *VmMessageWarningEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmMessageWarningEvent]**](VmMessageWarningEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_message_warning_event import ArrayOfVmMessageWarningEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmMessageWarningEvent from a JSON string
array_of_vm_message_warning_event_instance = ArrayOfVmMessageWarningEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmMessageWarningEvent.to_json()

# convert the object into a dict
array_of_vm_message_warning_event_dict = array_of_vm_message_warning_event_instance.to_dict()
# create an instance of ArrayOfVmMessageWarningEvent from a dict
array_of_vm_message_warning_event_form_dict = array_of_vm_message_warning_event.from_dict(array_of_vm_message_warning_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


