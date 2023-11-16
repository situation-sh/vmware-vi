# ArrayOfGeneralVmWarningEvent

A boxed array of *GeneralVmWarningEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GeneralVmWarningEvent]**](GeneralVmWarningEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_general_vm_warning_event import ArrayOfGeneralVmWarningEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfGeneralVmWarningEvent from a JSON string
array_of_general_vm_warning_event_instance = ArrayOfGeneralVmWarningEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfGeneralVmWarningEvent.to_json()

# convert the object into a dict
array_of_general_vm_warning_event_dict = array_of_general_vm_warning_event_instance.to_dict()
# create an instance of ArrayOfGeneralVmWarningEvent from a dict
array_of_general_vm_warning_event_form_dict = array_of_general_vm_warning_event.from_dict(array_of_general_vm_warning_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


