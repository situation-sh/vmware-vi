# VmDasUpdateErrorEvent

The event records that an error occurred when updating the HA agents with the current state of the virtual machine.  If this occurs during a powerOn operation, the virtual machine will not be failed over in the event of a host failure. If it occurs during a powerOff, the virtual machine will be automatically powered on if the host it was last running on crashes. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_das_update_error_event import VmDasUpdateErrorEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmDasUpdateErrorEvent from a JSON string
vm_das_update_error_event_instance = VmDasUpdateErrorEvent.from_json(json)
# print the JSON string representation of the object
print VmDasUpdateErrorEvent.to_json()

# convert the object into a dict
vm_das_update_error_event_dict = vm_das_update_error_event_instance.to_dict()
# create an instance of VmDasUpdateErrorEvent from a dict
vm_das_update_error_event_form_dict = vm_das_update_error_event.from_dict(vm_das_update_error_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


