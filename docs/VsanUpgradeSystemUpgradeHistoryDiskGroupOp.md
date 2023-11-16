# VsanUpgradeSystemUpgradeHistoryDiskGroupOp

The upgrade process removed or added VSAN from/to a disk group.  Class provides details about the operation and the disk group.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | Type of the operation, e.g.  add or remove.  See also *VsanUpgradeSystemUpgradeHistoryDiskGroupOpType_enum*.  ***Since:*** vSphere API 6.0  | 
**disk_mapping** | [**VsanHostDiskMapping**](VsanHostDiskMapping.md) |  | 

## Example

```python
from vmware_vi.models.vsan_upgrade_system_upgrade_history_disk_group_op import VsanUpgradeSystemUpgradeHistoryDiskGroupOp

# TODO update the JSON string below
json = "{}"
# create an instance of VsanUpgradeSystemUpgradeHistoryDiskGroupOp from a JSON string
vsan_upgrade_system_upgrade_history_disk_group_op_instance = VsanUpgradeSystemUpgradeHistoryDiskGroupOp.from_json(json)
# print the JSON string representation of the object
print VsanUpgradeSystemUpgradeHistoryDiskGroupOp.to_json()

# convert the object into a dict
vsan_upgrade_system_upgrade_history_disk_group_op_dict = vsan_upgrade_system_upgrade_history_disk_group_op_instance.to_dict()
# create an instance of VsanUpgradeSystemUpgradeHistoryDiskGroupOp from a dict
vsan_upgrade_system_upgrade_history_disk_group_op_form_dict = vsan_upgrade_system_upgrade_history_disk_group_op.from_dict(vsan_upgrade_system_upgrade_history_disk_group_op_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


