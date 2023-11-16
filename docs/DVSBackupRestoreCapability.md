# DVSBackupRestoreCapability

The *DVSBackupRestoreCapability* data object describes backup, restore, and rollback capabilities for distributed virtual switches and distributed virtual portgroups.  Backup and restore capabilities are indicated for *DistributedVirtualSwitch*. Rollback capability is indicated for *DistributedVirtualSwitch* and *DistributedVirtualPortgroup*.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_restore_supported** | **bool** | Indicates whether backup, restore, and rollback are supported.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.dvs_backup_restore_capability import DVSBackupRestoreCapability

# TODO update the JSON string below
json = "{}"
# create an instance of DVSBackupRestoreCapability from a JSON string
dvs_backup_restore_capability_instance = DVSBackupRestoreCapability.from_json(json)
# print the JSON string representation of the object
print DVSBackupRestoreCapability.to_json()

# convert the object into a dict
dvs_backup_restore_capability_dict = dvs_backup_restore_capability_instance.to_dict()
# create an instance of DVSBackupRestoreCapability from a dict
dvs_backup_restore_capability_form_dict = dvs_backup_restore_capability.from_dict(dvs_backup_restore_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


