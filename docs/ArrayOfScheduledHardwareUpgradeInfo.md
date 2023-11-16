# ArrayOfScheduledHardwareUpgradeInfo

A boxed array of *ScheduledHardwareUpgradeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ScheduledHardwareUpgradeInfo]**](ScheduledHardwareUpgradeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_scheduled_hardware_upgrade_info import ArrayOfScheduledHardwareUpgradeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfScheduledHardwareUpgradeInfo from a JSON string
array_of_scheduled_hardware_upgrade_info_instance = ArrayOfScheduledHardwareUpgradeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfScheduledHardwareUpgradeInfo.to_json()

# convert the object into a dict
array_of_scheduled_hardware_upgrade_info_dict = array_of_scheduled_hardware_upgrade_info_instance.to_dict()
# create an instance of ArrayOfScheduledHardwareUpgradeInfo from a dict
array_of_scheduled_hardware_upgrade_info_form_dict = array_of_scheduled_hardware_upgrade_info.from_dict(array_of_scheduled_hardware_upgrade_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


