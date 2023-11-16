# ScheduledHardwareUpgradeInfo

Data object type containing settings for the scheduled hardware upgrades.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upgrade_policy** | **str** | Scheduled hardware upgrade policy setting for the virtual machine.  See also *ScheduledHardwareUpgradeInfoHardwareUpgradePolicy_enum*.  ***Since:*** vSphere API 5.1  | [optional] 
**version_key** | **str** | Key for target hardware version to be used on next scheduled upgrade in the format of *VirtualMachineConfigOptionDescriptor.key*.  ***Since:*** vSphere API 5.1  | [optional] 
**scheduled_hardware_upgrade_status** | **str** | Status for last attempt to run scheduled hardware upgrade.  See also *ScheduledHardwareUpgradeInfoHardwareUpgradeStatus_enum*.  ***Since:*** vSphere API 5.1  | [optional] 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.scheduled_hardware_upgrade_info import ScheduledHardwareUpgradeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledHardwareUpgradeInfo from a JSON string
scheduled_hardware_upgrade_info_instance = ScheduledHardwareUpgradeInfo.from_json(json)
# print the JSON string representation of the object
print ScheduledHardwareUpgradeInfo.to_json()

# convert the object into a dict
scheduled_hardware_upgrade_info_dict = scheduled_hardware_upgrade_info_instance.to_dict()
# create an instance of ScheduledHardwareUpgradeInfo from a dict
scheduled_hardware_upgrade_info_form_dict = scheduled_hardware_upgrade_info.from_dict(scheduled_hardware_upgrade_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


