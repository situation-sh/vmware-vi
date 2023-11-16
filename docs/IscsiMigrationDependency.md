# IscsiMigrationDependency

Provides migration dependency information for a given Physical NIC.  Lists all the iSCSI and networking resources impacted if migration of a given Physical NIC is to take place.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migration_allowed** | **bool** | Indicates whether migration can be safely performed If migrationAllowed is False, the disallowReason will contain the specific condition that makes the migration attempt unsafe.  ***Since:*** vSphere API 5.0  | 
**disallow_reason** | [**IscsiStatus**](IscsiStatus.md) |  | [optional] 
**dependency** | [**List[IscsiDependencyEntity]**](IscsiDependencyEntity.md) | Details of all the resources affected by migration.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.iscsi_migration_dependency import IscsiMigrationDependency

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiMigrationDependency from a JSON string
iscsi_migration_dependency_instance = IscsiMigrationDependency.from_json(json)
# print the JSON string representation of the object
print IscsiMigrationDependency.to_json()

# convert the object into a dict
iscsi_migration_dependency_dict = iscsi_migration_dependency_instance.to_dict()
# create an instance of IscsiMigrationDependency from a dict
iscsi_migration_dependency_form_dict = iscsi_migration_dependency.from_dict(iscsi_migration_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


