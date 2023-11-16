# ClusterMigrationAction

Describes a single VM migration action.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drs_migration** | [**ClusterDrsMigration**](ClusterDrsMigration.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_migration_action import ClusterMigrationAction

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterMigrationAction from a JSON string
cluster_migration_action_instance = ClusterMigrationAction.from_json(json)
# print the JSON string representation of the object
print ClusterMigrationAction.to_json()

# convert the object into a dict
cluster_migration_action_dict = cluster_migration_action_instance.to_dict()
# create an instance of ClusterMigrationAction from a dict
cluster_migration_action_form_dict = cluster_migration_action.from_dict(cluster_migration_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


