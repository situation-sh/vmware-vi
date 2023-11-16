# VsanUpgradeSystemUpgradeHistoryPreflightFail

Upgrade process encountered a pre-flight check failure.  This leads to the upgrade process aborting the upgrade.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preflight_result** | [**VsanUpgradeSystemPreflightCheckResult**](VsanUpgradeSystemPreflightCheckResult.md) |  | 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_upgrade_history_preflight_fail import VsanUpgradeSystemUpgradeHistoryPreflightFail

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemUpgradeHistoryPreflightFail from a JSON string
vsan_upgrade_system_upgrade_history_preflight_fail_instance = VsanUpgradeSystemUpgradeHistoryPreflightFail.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemUpgradeHistoryPreflightFail.to_json()

# convert the object into a dict
vsan_upgrade_system_upgrade_history_preflight_fail_dict = vsan_upgrade_system_upgrade_history_preflight_fail_instance.to_dict()
# create an instance of VsanUpgradeSystemUpgradeHistoryPreflightFail from a dict
vsan_upgrade_system_upgrade_history_preflight_fail_form_dict = vsan_upgrade_system_upgrade_history_preflight_fail.from_dict(vsan_upgrade_system_upgrade_history_preflight_fail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


