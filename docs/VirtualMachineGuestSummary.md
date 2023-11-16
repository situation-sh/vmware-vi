# VirtualMachineGuestSummary

A subset of virtual machine guest information. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_id** | **str** | Guest operating system identifier (short name), if known.  | [optional] 
**guest_full_name** | **str** | Guest operating system name configured on the virtual machine.  | [optional] 
**tools_status** | [**VirtualMachineToolsStatusEnum**](VirtualMachineToolsStatusEnum.md) |  | [optional] 
**tools_version_status** | **str** | Deprecated as of vSphere API 5.0 use *VirtualMachineGuestSummary.toolsVersionStatus2*.  Current version status of VMware Tools in the guest operating system, if known.  ***Since:*** vSphere API 4.0  | [optional] 
**tools_version_status2** | **str** | Current version status of VMware Tools in the guest operating system, if known.  ***Since:*** vSphere API 5.0  | [optional] 
**tools_running_status** | **str** | Current running status of VMware Tools in the guest operating system, if known.  ***Since:*** vSphere API 4.0  | [optional] 
**host_name** | **str** | Hostname of the guest operating system, if known.  | [optional] 
**ip_address** | **str** | Primary IP address assigned to the guest operating system, if known.  | [optional] 
**hw_version** | **str** | The hardware version string for this virtual machine.  ***Since:*** vSphere API 6.9.1  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_guest_summary import VirtualMachineGuestSummary

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineGuestSummary from a JSON string
virtual_machine_guest_summary_instance = VirtualMachineGuestSummary.from_json(json)
# print the JSON string representation of the object
print VirtualMachineGuestSummary.to_json()

# convert the object into a dict
virtual_machine_guest_summary_dict = virtual_machine_guest_summary_instance.to_dict()
# create an instance of VirtualMachineGuestSummary from a dict
virtual_machine_guest_summary_form_dict = virtual_machine_guest_summary.from_dict(virtual_machine_guest_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


