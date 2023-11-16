# ArrayOfVirtualMachineGuestMonitoringModeInfo

A boxed array of *VirtualMachineGuestMonitoringModeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineGuestMonitoringModeInfo]**](VirtualMachineGuestMonitoringModeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_guest_monitoring_mode_info import ArrayOfVirtualMachineGuestMonitoringModeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineGuestMonitoringModeInfo from a JSON string
array_of_virtual_machine_guest_monitoring_mode_info_instance = ArrayOfVirtualMachineGuestMonitoringModeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineGuestMonitoringModeInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_guest_monitoring_mode_info_dict = array_of_virtual_machine_guest_monitoring_mode_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineGuestMonitoringModeInfo from a dict
array_of_virtual_machine_guest_monitoring_mode_info_form_dict = array_of_virtual_machine_guest_monitoring_mode_info.from_dict(array_of_virtual_machine_guest_monitoring_mode_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


