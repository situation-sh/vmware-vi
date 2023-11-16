# VsanUpgradeSystemUpgradeStatus

Captures the status of a VSAN cluster on-disk format upgrade.  Contains information about progress, result, and a detailed log of operations.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_progress** | **bool** | True if there is an active upgrade process.  If true, other fields are guaranteed to be populated. If false, other fields may reflect a previous upgrade process run, or they may be unset.  ***Since:*** vSphere API 6.0  | 
**history** | [**List[VsanUpgradeSystemUpgradeHistoryItem]**](VsanUpgradeSystemUpgradeHistoryItem.md) | Log of a single upgrade task.  Lists all operations performed by the upgrade process in chronological order.  ***Since:*** vSphere API 6.0  | [optional] 
**aborted** | **bool** | Set if the upgrade process was aborted.  ***Since:*** vSphere API 6.0  | [optional] 
**completed** | **bool** | Set if the upgrade process has completed successfully.  ***Since:*** vSphere API 6.0  | [optional] 
**progress** | **int** | Progress in percent.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_upgrade_status import VsanUpgradeSystemUpgradeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemUpgradeStatus from a JSON string
vsan_upgrade_system_upgrade_status_instance = VsanUpgradeSystemUpgradeStatus.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemUpgradeStatus.to_json()

# convert the object into a dict
vsan_upgrade_system_upgrade_status_dict = vsan_upgrade_system_upgrade_status_instance.to_dict()
# create an instance of VsanUpgradeSystemUpgradeStatus from a dict
vsan_upgrade_system_upgrade_status_form_dict = vsan_upgrade_system_upgrade_status.from_dict(vsan_upgrade_system_upgrade_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


