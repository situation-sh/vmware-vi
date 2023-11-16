# VirtualMachineDefaultPowerOpInfo

The DefaultPowerOpInfo data object type holds the configured defaults for the power operations on a virtual machine.  The properties indicated whether to do a \"soft\" or guest initiated operation, or a \"hard\" operation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**power_off_type** | **str** | Describes the default power off type for this virtual machine.  The possible values are specified by the PowerOpType. - hard - Perform power off by using the PowerOff method. - soft - Perform power off by using the ShutdownGuest method. - preset - The preset value is specified in the defaultPowerOffType   section.    This setting is advisory and clients can choose to ignore it.  | [optional] 
**suspend_type** | **str** | Describes the default suspend type for this virtual machine.  The possible values are specified by the PowerOpType. - hard - Perform suspend by using the Suspend method. - soft - Perform suspend by using the StandbyGuest method. - preset - The preset value is specified in the defaultSuspendType   section.    This setting is advisory and clients can choose to ignore it.  | [optional] 
**reset_type** | **str** | Describes the default reset type for this virtual machine.  The possible values are specified by the PowerOpType. - hard - Perform reset by using the Reset method. - soft - Perform reset by using the RebootGuest method. - preset - The preset value is specified in the defaultResetType   section.    This setting is advisory and clients can choose to ignore it.  | [optional] 
**default_power_off_type** | **str** | Default operation for power off: soft or hard  | [optional] 
**default_suspend_type** | **str** | Default operation for suspend: soft or hard  | [optional] 
**default_reset_type** | **str** | Default operation for reset: soft or hard  | [optional] 
**standby_action** | **str** | Behavior of virtual machine when it receives the S1 ACPI call.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_default_power_op_info import VirtualMachineDefaultPowerOpInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineDefaultPowerOpInfo from a JSON string
virtual_machine_default_power_op_info_instance = VirtualMachineDefaultPowerOpInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineDefaultPowerOpInfo.to_json()

# convert the object into a dict
virtual_machine_default_power_op_info_dict = virtual_machine_default_power_op_info_instance.to_dict()
# create an instance of VirtualMachineDefaultPowerOpInfo from a dict
virtual_machine_default_power_op_info_form_dict = virtual_machine_default_power_op_info.from_dict(virtual_machine_default_power_op_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


