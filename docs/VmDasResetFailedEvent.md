# VmDasResetFailedEvent

This event records when HA VM Health Monitoring fails to reset a virtual machine after failure  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_das_reset_failed_event import VmDasResetFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmDasResetFailedEvent from a JSON string
vm_das_reset_failed_event_instance = VmDasResetFailedEvent.from_json(json)
# print the JSON string representation of the object
print VmDasResetFailedEvent.to_json()

# convert the object into a dict
vm_das_reset_failed_event_dict = vm_das_reset_failed_event_instance.to_dict()
# create an instance of VmDasResetFailedEvent from a dict
vm_das_reset_failed_event_form_dict = vm_das_reset_failed_event.from_dict(vm_das_reset_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


