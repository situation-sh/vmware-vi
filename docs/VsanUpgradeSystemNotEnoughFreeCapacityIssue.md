# VsanUpgradeSystemNotEnoughFreeCapacityIssue

Pre-flight check encountered not enough free disk capacity to maintain policy compliance.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reduced_redundancy_upgrade_possible** | **bool** | Indicates that whether upgrade could be processed if option allowReducedRedundancy is taken.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_not_enough_free_capacity_issue import VsanUpgradeSystemNotEnoughFreeCapacityIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemNotEnoughFreeCapacityIssue from a JSON string
vsan_upgrade_system_not_enough_free_capacity_issue_instance = VsanUpgradeSystemNotEnoughFreeCapacityIssue.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemNotEnoughFreeCapacityIssue.to_json()

# convert the object into a dict
vsan_upgrade_system_not_enough_free_capacity_issue_dict = vsan_upgrade_system_not_enough_free_capacity_issue_instance.to_dict()
# create an instance of VsanUpgradeSystemNotEnoughFreeCapacityIssue from a dict
vsan_upgrade_system_not_enough_free_capacity_issue_form_dict = vsan_upgrade_system_not_enough_free_capacity_issue.from_dict(vsan_upgrade_system_not_enough_free_capacity_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


