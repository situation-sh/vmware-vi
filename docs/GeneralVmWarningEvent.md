# GeneralVmWarningEvent

This event is the general warning event for a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.general_vm_warning_event import GeneralVmWarningEvent

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralVmWarningEvent from a JSON string
general_vm_warning_event_instance = GeneralVmWarningEvent.from_json(json)
# print the JSON string representation of the object
print GeneralVmWarningEvent.to_json()

# convert the object into a dict
general_vm_warning_event_dict = general_vm_warning_event_instance.to_dict()
# create an instance of GeneralVmWarningEvent from a dict
general_vm_warning_event_form_dict = general_vm_warning_event.from_dict(general_vm_warning_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


