# VsanUpgradeSystemUpgradeHistoryItem

Captures one \"log entry\" of an upgrade process.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** | Time stamp when the history is record.  ***Since:*** vSphere API 6.0  | 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**message** | **str** | Description of the history item.  ***Since:*** vSphere API 6.0  | 
**task** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_upgrade_history_item import VsanUpgradeSystemUpgradeHistoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemUpgradeHistoryItem from a JSON string
vsan_upgrade_system_upgrade_history_item_instance = VsanUpgradeSystemUpgradeHistoryItem.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemUpgradeHistoryItem.to_json()

# convert the object into a dict
vsan_upgrade_system_upgrade_history_item_dict = vsan_upgrade_system_upgrade_history_item_instance.to_dict()
# create an instance of VsanUpgradeSystemUpgradeHistoryItem from a dict
vsan_upgrade_system_upgrade_history_item_form_dict = vsan_upgrade_system_upgrade_history_item.from_dict(vsan_upgrade_system_upgrade_history_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


