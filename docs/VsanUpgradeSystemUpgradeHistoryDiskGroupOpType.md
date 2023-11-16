# VsanUpgradeSystemUpgradeHistoryDiskGroupOpType

A boxed *VsanUpgradeSystemUpgradeHistoryDiskGroupOpType_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VsanUpgradeSystemUpgradeHistoryDiskGroupOpTypeEnum**](VsanUpgradeSystemUpgradeHistoryDiskGroupOpTypeEnum.md) |  | 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_upgrade_history_disk_group_op_type import VsanUpgradeSystemUpgradeHistoryDiskGroupOpType

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemUpgradeHistoryDiskGroupOpType from a JSON string
vsan_upgrade_system_upgrade_history_disk_group_op_type_instance = VsanUpgradeSystemUpgradeHistoryDiskGroupOpType.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemUpgradeHistoryDiskGroupOpType.to_json()

# convert the object into a dict
vsan_upgrade_system_upgrade_history_disk_group_op_type_dict = vsan_upgrade_system_upgrade_history_disk_group_op_type_instance.to_dict()
# create an instance of VsanUpgradeSystemUpgradeHistoryDiskGroupOpType from a dict
vsan_upgrade_system_upgrade_history_disk_group_op_type_form_dict = vsan_upgrade_system_upgrade_history_disk_group_op_type.from_dict(vsan_upgrade_system_upgrade_history_disk_group_op_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


