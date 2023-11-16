# HostLowLevelProvisioningManagerVmMigrationStatus

The status of a virtual machine migration operation.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_id** | **int** | Unique identifier for this operation, currently it&#39;s unique within one virtual center instance.  ***Since:*** vSphere API 5.1  | 
**type** | **str** | Manner in which the migration process is performed.  The set of possible values is described in *HostVMotionManagerVMotionType_enum*.  ***Since:*** vSphere API 5.1  | 
**source** | **bool** | Whether the virtual machine is the source of the migration.  For disk only migration, the value is always true.  ***Since:*** vSphere API 5.1  | 
**considered_successful** | **bool** | Whether the operation is considered successful.  A migration operation is considered successful if its switch over phase has completed successfully.  More specifically, for an in-progress migration, it is considered successful if it has had a sucessful switch over, otherwise it is considered unsuccessful. Likewise, the status of a completed migration operation is also based on the switch over completion status.  The difference between a completed vs. in-progress migration with the same consideredSuccessful property is that in the former case the server is able to complete the clean up process thus leaves nothing for the recovery process to clean up.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.host_low_level_provisioning_manager_vm_migration_status import HostLowLevelProvisioningManagerVmMigrationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of HostLowLevelProvisioningManagerVmMigrationStatus from a JSON string
host_low_level_provisioning_manager_vm_migration_status_instance = HostLowLevelProvisioningManagerVmMigrationStatus.from_json(json)
# print the JSON string representation of the object
print HostLowLevelProvisioningManagerVmMigrationStatus.to_json()

# convert the object into a dict
host_low_level_provisioning_manager_vm_migration_status_dict = host_low_level_provisioning_manager_vm_migration_status_instance.to_dict()
# create an instance of HostLowLevelProvisioningManagerVmMigrationStatus from a dict
host_low_level_provisioning_manager_vm_migration_status_form_dict = host_low_level_provisioning_manager_vm_migration_status.from_dict(host_low_level_provisioning_manager_vm_migration_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


