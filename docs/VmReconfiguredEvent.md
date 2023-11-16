# VmReconfiguredEvent

This event records a reconfiguration of the virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_spec** | [**VirtualMachineConfigSpec**](VirtualMachineConfigSpec.md) |  | 
**config_changes** | [**ChangesInfoEventArgument**](ChangesInfoEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_reconfigured_event import VmReconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmReconfiguredEvent from a JSON string
vm_reconfigured_event_instance = VmReconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print VmReconfiguredEvent.to_json()

# convert the object into a dict
vm_reconfigured_event_dict = vm_reconfigured_event_instance.to_dict()
# create an instance of VmReconfiguredEvent from a dict
vm_reconfigured_event_form_dict = vm_reconfigured_event.from_dict(vm_reconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


