# VmDasBeingResetEvent

This event records when a virtual machine is reset by HA VM Health Monitoring on hosts that do not support the create screenshot api or if the createscreenshot api fails.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason why this vm is being reset  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.vm_das_being_reset_event import VmDasBeingResetEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmDasBeingResetEvent from a JSON string
vm_das_being_reset_event_instance = VmDasBeingResetEvent.from_json(json)
# print the JSON string representation of the object
print VmDasBeingResetEvent.to_json()

# convert the object into a dict
vm_das_being_reset_event_dict = vm_das_being_reset_event_instance.to_dict()
# create an instance of VmDasBeingResetEvent from a dict
vm_das_being_reset_event_form_dict = vm_das_being_reset_event.from_dict(vm_das_being_reset_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


