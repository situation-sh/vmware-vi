# HbrDiskMigrationAction

Describes a single HBR secondary disk migration action.  The storage migration action applies either to a single disk or a set of secondary virtual disks.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_id** | **str** | HMS Service specific collection id  ***Since:*** vSphere API 6.0  | 
**collection_name** | **str** | HMS specific name of this collection  ***Since:*** vSphere API 6.0  | 
**disk_ids** | **List[str]** | HBR disk ids of secondary disks moved by this action  ***Since:*** vSphere API 6.0  | 
**source** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**destination** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**size_transferred** | **int** | The amount of data to be transferred.  Unit: KB.  ***Since:*** vSphere API 6.0  | 
**space_util_src_before** | **float** | Space utilization on the source datastore before storage migration.  Unit: percentage. For example, if set to 70.0, space utilization is 70%. If not set, the value is not available.  ***Since:*** vSphere API 6.0  | [optional] 
**space_util_dst_before** | **float** | Space utilization on the destination datastore before storage migration.  Unit: percentage. For example, if set to 70.0, space utilization is 70%. If not set, the value is not available.  ***Since:*** vSphere API 6.0  | [optional] 
**space_util_src_after** | **float** | Expected space utilization on the source datastore after storage migration.  Unit: percentage. For example, if set to 70.0, space utilization is 70%. If not set, the value is not available.  ***Since:*** vSphere API 6.0  | [optional] 
**space_util_dst_after** | **float** | Expected space utilization on the destination datastore after storage migration.  Unit: percentage. For example, if set to 70.0, space utilization is 70%. If not set, the value is not available.  ***Since:*** vSphere API 6.0  | [optional] 
**io_latency_src_before** | **float** | I/O latency on the source datastore before storage migration.  Unit: millisecond. If not set, the value is not available.  ***Since:*** vSphere API 6.0  | [optional] 
**io_latency_dst_before** | **float** | I/O latency on the destination datastore before storage migration.  Unit: millisecond. If not set, the value is not available.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.hbr_disk_migration_action import HbrDiskMigrationAction

# TODO update the JSON string below
json = "{}"
# create an instance of HbrDiskMigrationAction from a JSON string
hbr_disk_migration_action_instance = HbrDiskMigrationAction.from_json(json)
# print the JSON string representation of the object
print HbrDiskMigrationAction.to_json()

# convert the object into a dict
hbr_disk_migration_action_dict = hbr_disk_migration_action_instance.to_dict()
# create an instance of HbrDiskMigrationAction from a dict
hbr_disk_migration_action_form_dict = hbr_disk_migration_action.from_dict(hbr_disk_migration_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


