# VirtualMachineGuestMonitoringModeInfo

This data object describes the GMM (Guest Mode Monitoring) configuration of this virtual machine.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gmm_file** | **str** |  | [optional] 
**gmm_appliance** | **str** |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_guest_monitoring_mode_info import VirtualMachineGuestMonitoringModeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineGuestMonitoringModeInfo from a JSON string
virtual_machine_guest_monitoring_mode_info_instance = VirtualMachineGuestMonitoringModeInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineGuestMonitoringModeInfo.to_json()

# convert the object into a dict
virtual_machine_guest_monitoring_mode_info_dict = virtual_machine_guest_monitoring_mode_info_instance.to_dict()
# create an instance of VirtualMachineGuestMonitoringModeInfo from a dict
virtual_machine_guest_monitoring_mode_info_form_dict = virtual_machine_guest_monitoring_mode_info.from_dict(virtual_machine_guest_monitoring_mode_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


