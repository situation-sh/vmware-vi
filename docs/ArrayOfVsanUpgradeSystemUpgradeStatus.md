# ArrayOfVsanUpgradeSystemUpgradeStatus

A boxed array of *VsanUpgradeSystemUpgradeStatus*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanUpgradeSystemUpgradeStatus]**](VsanUpgradeSystemUpgradeStatus.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_upgrade_system_upgrade_status import ArrayOfVsanUpgradeSystemUpgradeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanUpgradeSystemUpgradeStatus from a JSON string
array_of_vsan_upgrade_system_upgrade_status_instance = ArrayOfVsanUpgradeSystemUpgradeStatus.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanUpgradeSystemUpgradeStatus.to_json()

# convert the object into a dict
array_of_vsan_upgrade_system_upgrade_status_dict = array_of_vsan_upgrade_system_upgrade_status_instance.to_dict()
# create an instance of ArrayOfVsanUpgradeSystemUpgradeStatus from a dict
array_of_vsan_upgrade_system_upgrade_status_form_dict = array_of_vsan_upgrade_system_upgrade_status.from_dict(array_of_vsan_upgrade_system_upgrade_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


