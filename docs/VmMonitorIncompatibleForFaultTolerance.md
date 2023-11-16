# VmMonitorIncompatibleForFaultTolerance

Thrown when turning on Fault Tolerance protection on a running virtual machine if the virtual machine is running in a monitor mode that is incompatible.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_monitor_incompatible_for_fault_tolerance import VmMonitorIncompatibleForFaultTolerance

# TODO update the JSON string below
json = "{}"
# create an instance of VmMonitorIncompatibleForFaultTolerance from a JSON string
vm_monitor_incompatible_for_fault_tolerance_instance = VmMonitorIncompatibleForFaultTolerance.from_json(json)
# print the JSON string representation of the object
print VmMonitorIncompatibleForFaultTolerance.to_json()

# convert the object into a dict
vm_monitor_incompatible_for_fault_tolerance_dict = vm_monitor_incompatible_for_fault_tolerance_instance.to_dict()
# create an instance of VmMonitorIncompatibleForFaultTolerance from a dict
vm_monitor_incompatible_for_fault_tolerance_form_dict = vm_monitor_incompatible_for_fault_tolerance.from_dict(vm_monitor_incompatible_for_fault_tolerance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


