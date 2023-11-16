# GeneralVmInfoEvent

This event is the general information event for a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.general_vm_info_event import GeneralVmInfoEvent

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralVmInfoEvent from a JSON string
general_vm_info_event_instance = GeneralVmInfoEvent.from_json(json)
# print the JSON string representation of the object
print GeneralVmInfoEvent.to_json()

# convert the object into a dict
general_vm_info_event_dict = general_vm_info_event_instance.to_dict()
# create an instance of GeneralVmInfoEvent from a dict
general_vm_info_event_form_dict = general_vm_info_event.from_dict(general_vm_info_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


